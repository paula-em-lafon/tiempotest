import React, { Component } from 'react';
import styles from './App.module.css';
import { Card } from 'react-bootstrap';
import dateFormat from 'dateformat';
import 'bootstrap/dist/css/bootstrap.min.css'

class App extends Component {


  state = {
    results: null,
    total: null,
    total_pages: null,
    per_page: null,
    current_page: 1
  }


  componentDidMount() {
    this.makeHttpRequestWithPage(1);
  }

  makeHttpRequestWithPage = async pageNumber => {
    const response = await fetch(`http://127.0.0.1:8000/cfdilist/?page=${pageNumber}`, {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
    });

    const data = await response.json();

    this.setState({
      results: data.results,
      total: data.total,
      total_pages: data.total_pages,
      per_page: data.page_size,
      current_page: data.page
    });
  }


  render() {
    console.dir(this.state.results)

    let results, renderPageNumbers;

    if (this.state.results !== null) {
      results = this.state.results.map(result => (
        <Card>
          <Card.Title>entry: {result.id}</Card.Title>
          <Card.Text><b>Name:</b> {result.issuer_name}</Card.Text>
          <Card.Text><b>Date:</b> {dateFormat(result.date_issued, "mmmm dS, yyyy")}</Card.Text>
          <Card.Text><b>RFC:</b> {result.issuer_rfc}</Card.Text>
          <Card.Text><b>Ammount:</b> {result.total_ammount}$</Card.Text>
          <Card.Text><b>cfdi XML:</b></Card.Text>
          <textarea>{result.cfdi_xml}</textarea>
        </Card>
      ));
    }

    const pageNumbers = [];
    if (this.state.total !== null) {
      for (let i = 1; i <= this.state.total_pages; i++) {
        pageNumbers.push(i);
      }


      renderPageNumbers = pageNumbers.map(number => {
        let classes = this.state.current_page === number ? styles.active : '';

        if (number === 1 || number === this.state.total || (number >= this.state.current_page - 2 && number <= this.state.current_page + 2)) {
          return (
            <span key={number} className={classes} onClick={() => this.makeHttpRequestWithPage(number)}>{number}</span>
          );
        }
      });
    }

    return (
      

      <div className={styles.app}>
          {results}
        <div className={styles.pagination}>
          <span onClick={() => this.makeHttpRequestWithPage(1)}>&laquo;</span>
          {renderPageNumbers}
          <span onClick={() => this.makeHttpRequestWithPage(1)}>&raquo;</span>
        </div>

      </div>
    );
  }

}

export default App;