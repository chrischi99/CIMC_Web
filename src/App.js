import './UI.css';
import React, { Component } from 'react';
import axios from 'axios';
import { MdDashboard } from "react-icons/md";
import {MdSearch} from "react-icons/md";
import {MdKeyboardReturn} from "react-icons/md";
import {AiOutlineSearch} from "react-icons/md";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      events: null,
      curTime : new Date().toLocaleString(),
      searchfield: '',
      previous: []
    }
  }
  
  componentWillMount() {
    const url = `http://127.0.0.1:5000/`;
    axios.get(url).then((response => response.data))
    .then((data) => {
      this.setState({ news: data })
     })
  }

  render () {
    var all_news = this.state.news
    if (!this.state.news) {
      return <div className = "background_loading"><span className = "loading_page">Loading...</span></div>;
    }

    const ColoredLine = ({ color }) => (
      <hr
          style={{
              color: color,
              backgroundColor: color,
              width: '150px'
          }}
      />
      
  );

    return (
      <div className = "container">
        <img className = "top_logo" src = 'http://www.cimc.com/shtml/assets/images/logo.png' alt="Smiley face"/>
        <div className = "web_title_location"><p className = "web_title">实时资讯</p></div>
        <div className = "line_1"><ColoredLine color="lightblue" /></div>
        <p className = "data_time">数据时间 : {this.state.curTime}</p>
        <div className = "line_2" ><ColoredLine color="lightblue" /></div>
        {all_news.map(news => (
          
        <Link class="nav-link" to={{
          pathname: "/each_new",
          url: news['url'], // your data array of objects
          previous : "/"
        }}>
          <div className = "each_news">
            <span><img className = "preview_pic" src = {news['picurl']} alt="Smiley face"/></span>
            <span className = "title">{news['title']} </span>
            <span className = "media_name">{news['media_name']}</span>
            <span className = "time">{news['publish_time']}</span>
          </div>
        </Link>
        ))}
        <div className = "padding"></div>
        <div className = "menu_bar">
              <Link class="nav-link" to="/"><span className = "dashboard_active"><MdDashboard size={38}/></span></Link>
              <Link class="nav-link" to={{
                  pathname: "/query",
                  previous : "/"
                }}><span className = "query"><MdSearch size={38}/></span></Link>
              <Link class="nav-link" to={{
                pathname: this.props.location.previous
              }}><span className = "return"><MdKeyboardReturn size={38}/></span></Link>
              <br></br>
              <Link class="nav-link" to="/"><span className = "dashboard_word" >首页</span></Link>
              <Link class="nav-link" to={{
                  pathname: "/query",
                  previous : "/"
                }}><span className = "query_word">搜索</span></Link>
              <Link class="nav-link" to={{
                pathname: this.props.location.previous
              }}><span className = "return_word">返回</span></Link>
        </div>
    </div>
    );
  }
}

class Query extends Component {
  constructor(props) {
    super(props);
    this.state = {
      events: null,
      curTime : new Date().toLocaleString(),
      searchfield: '',
      value: '',
      previous: []
    }
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    // alert('A keyword was submitted: ' + this.state.value);
    event.preventDefault();
    this.setState({searchfield: this.state.value});
    var myParams = {
      data: this.state.value
    }
    if (myParams != "") {
    axios.post('http://127.0.0.1:5000/', myParams)
    .then(response => response.data)
    .then((data) => {
      this.setState({ news: data })
      this.setState({ events: true })
      console.log(this.state.news)
      if (!this.state.news) {
        return <span className = "loading_page"></span>;
      }
     })
  }
  }


  render () {
  if (this.state.news == null){
    return (
    <div className = "container_2">
      <img className = "top_logo" src = 'http://www.cimc.com/shtml/assets/images/logo.png' alt="Smiley face"/>
      <form className = "query_form_2" onSubmit={this.handleSubmit}>
        <input className = "input_field" type="text" value={this.state.value} onChange={this.handleChange} />
          <span className = "submit_button" ><button type = "submit"><MdSearch className = "search_button_logo"size={25}/></button></span>
      </form>
      <div className = "menu_bar">
            <Link class="nav-link" to={{
                  pathname: "/",
                  previous : "/query"
                }}><span className = "dashboard"><MdDashboard size={38}/></span></Link>
            <Link class="nav-link" to="/query"><span className = "query_active"><MdSearch size={38}/></span></Link>
            <Link class="nav-link" to={{
                pathname: this.props.location.previous
              }}><span className = "return"><MdKeyboardReturn size={38}/></span></Link>
            <br></br>
            <Link class="nav-link" to={{
                  pathname: "/",
                  previous : "/query"
                }}><span className = "dashboard_word" >首页</span></Link>
            <Link class="nav-link" to="/query"><span className = "query_word">搜索</span></Link>
            <Link class="nav-link" to={{
                pathname: this.props.location.previous
              }}><span className = "return_word">返回</span></Link>
      </div>  
    </div>
      );
  }
  else{
    return (
      <div className = "container_3">
        <img className = "top_logo" src = 'http://www.cimc.com/shtml/assets/images/logo.png' alt="Smiley face"/>
        <form className = "query_form_2" onSubmit={this.handleSubmit}>
        <input className = "input_field" type="text" value={this.state.value} onChange={this.handleChange} />
          <span className = "submit_button" ><button type = "submit"><MdSearch className = "search_button_logo"size={25}/></button></span>
      </form>

        {this.state.news.map(news => (
          <Link class="nav-link" to={{
          pathname: "/each_new",
          url: news['url'], // your data array of objects
          previous : "/"
        }}>
          <div className = "each_news">
            <span><img className = "preview_pic" src = {news['picurl']} alt="Smiley face"/></span>
            <span className = "title">{news['title']} </span>
            <span className = "media_name">{news['media_name']}</span>
            <span className = "time">{news['publish_time']}</span>
          </div>
        </Link>
        ))}
        <div className = "padding"></div>
        <div className = "menu_bar">
          <Link class="nav-link" to={{
                  pathname: "/",
                  previous : "/query"
                }}><span className = "dashboard"><MdDashboard size={38}/></span></Link>
            <Link class="nav-link" to="/query"><span className = "query_active"><MdSearch size={38}/></span></Link>
            <Link class="nav-link" to={{
                pathname: this.props.location.previous
              }}><span className = "return"><MdKeyboardReturn size={38}/></span></Link>
            <br></br>
            <Link class="nav-link" to={{
                  pathname: "/",
                  previous : "/query"
                }}><span className = "dashboard_word" >首页</span></Link>
            <Link class="nav-link" to="/query"><span className = "query_word">搜索</span></Link>
            <Link class="nav-link" to={{
                pathname: this.props.location.previous
              }}><span className = "return_word">返回</span></Link>
        </div>
    </div>
    );
  }
    
  }
}


class Each_news extends Component {
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
  render () {
    console.log(this.props)
    return (
      <div>
        <div className = "container_news">
        <img className = "top_logo_3" src = 'http://www.cimc.com/shtml/assets/images/logo.png' alt="Smiley face"/>
        </div>
        <iframe className="preview_pdf" width="420px" height="720px" src= {this.props.location.url}/>
        <div className = "menu_bar">
            <Link class="nav-link" to="/"><span className = "dashboard"><MdDashboard size={38}/></span></Link>
            <Link class="nav-link" to="/query"><span className = "query_active"><MdSearch size={38}/></span></Link>
            <Link class="nav-link" to={{
                pathname: this.props.location.previous
              }}><span className = "return"><MdKeyboardReturn size={38}/></span></Link>
            <br></br>
            <Link class="nav-link" to="/"><span className = "dashboard_word" >首页</span></Link>
            <Link class="nav-link" to="/query"><span className = "query_word">搜索</span></Link>
            <Link class="nav-link" to={{
                pathname: this.props.location.previous
              }}><span className = "return_word">返回</span></Link>
        </div>
    </div>
    );
  
    
  }
}

function App() {
  return (
    <div className="App">
      <Router>
          <Route path="/" exact component={Home} />
          <Route path="/query" exact component={Query} />
          <Route path="/each_new" exact component={Each_news} />
      </Router>
    </div>
  );
}


export default App;