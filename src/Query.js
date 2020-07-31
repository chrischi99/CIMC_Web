import './App.css';
import React, { Component } from 'react';
import axios from 'axios';
import { MdDashboard } from "react-icons/md";
import {MdSearch} from "react-icons/md";
import {MdKeyboardReturn} from "react-icons/md";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

class Query extends Component {
  constructor(props) {
    super(props);
    this.state = {
      events: null,
      curTime : new Date().toLocaleString(),
      searchfield: '',
      value: ''
    }
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    alert('A keyword was submitted: ' + this.state.value);
    event.preventDefault();
    this.setState({searchfield: this.state.value});
    var myParams = {
      data: this.state.searchfield
    }
    if (myParams != "") {
    axios.post('http://127.0.0.1:5000/', myParams)
    .then(response => response.data)
    .then((data) => {
      this.setState({ news: data })
      this.setState({ events: true })
      console.log(this.state.news)
      if (!this.state.news) {
        return <span>Loading...</span>;
      }
     })
  }
  }


  render () {
    const ColoredLine = ({ color }) => (
      <hr
          style={{
              color: color,
              backgroundColor: color,
              width: '150px'
          }}
      />
  );
  if (this.state.news == null){
    return (
    <div className = "container_2">
      <img className = "top_logo" src = 'http://www.cimc.com/shtml/assets/images/logo.png' alt="Smiley face"/>
      <form className = "query_form_2" onSubmit={this.handleSubmit}>
        <label>
        <input type="text" value={this.state.value} onChange={this.handleChange} />
        </label>
        <input className = "submit_button" type="submit" value="Submit" />
      </form>
      <div className = "menu_bar">
            <span className = "dashboard"><MdDashboard size={38}/></span>
            <span className = "query_active"><MdSearch size={38}/></span>
            <span className = "return"><MdKeyboardReturn size={38}/></span>
            <br></br>
            <span className = "dashboard_word" >首页</span>
            <span className = "query_word">搜索</span>
            <span className = "return_word">返回</span>
        </div>
    </div>

    
      );
  }
  else{
    return (
      <div className = "container_2">
        <img className = "top_logo" src = 'http://www.cimc.com/shtml/assets/images/logo.png' alt="Smiley face"/>
        <form className = "query_form" onSubmit={this.handleSubmit}>
          <label>
          <input className = "input_form" type="text" value={this.state.value} onChange={this.handleChange} />
          </label>
          <input className = "submit_button" type="submit" value="Submit" />
        </form>

        {this.state.news.map(news => (
          <a className = "url" href = {news['url']}>
          <div className = "each_news">
            <span><img className = "preview_pic" src = 'https://www.cimc.com/en/uploadfile/2016/0308/20160308114409462.jpg' alt="Smiley face"/></span>
            <span className = "title">{news['title']} </span>
            <span className = "media_name">{news['media_name']}</span>
            <span className = "time">{news['publish_time']}</span>
          </div>
        </a>
        ))}
        <div className = "padding"></div>
        <div className = "menu_bar">
            <span className = "dashboard"><MdDashboard size={38}/></span>
            <span className = "query_active"><MdSearch size={38}/></span>
            <span className = "return"><MdKeyboardReturn size={38}/></span>
            <br></br>
            <span className = "dashboard_word" >首页</span>
            <span className = "query_word">搜索</span>
            <span className = "return_word">返回</span>
        </div>
    </div>
    );
  }
    
  }
}


export default Query;
