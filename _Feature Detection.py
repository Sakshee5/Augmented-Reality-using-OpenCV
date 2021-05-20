<!DOCTYPE html>
<!-- saved from url=(0086)http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py# -->
<html lang="en-us"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    

    <title>*Feature Detection.py - Jupyter Text Editor</title>
    <link id="favicon" rel="shortcut icon" type="image/x-icon" href="http://localhost:8888/static/base/images/favicon-file.ico?v=e2776a7f45692c839d6eea7d7ff6f3b2">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="stylesheet" href="./_Feature Detection_files/jquery-ui.min.css" type="text/css">
    <link rel="stylesheet" href="./_Feature Detection_files/jquery.typeahead.min.css" type="text/css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    
<link rel="stylesheet" href="./_Feature Detection_files/codemirror.css">
<link rel="stylesheet" href="./_Feature Detection_files/dialog.css">

    <link rel="stylesheet" href="./_Feature Detection_files/style.min.css" type="text/css">
    

    <link rel="stylesheet" href="./_Feature Detection_files/custom.css" type="text/css">
    <script src="./_Feature Detection_files/promise.min.js.download" type="text/javascript" charset="utf-8"></script>
    <script src="./_Feature Detection_files/react.production.min.js.download" type="text/javascript"></script>
    <script src="./_Feature Detection_files/react-dom.production.min.js.download" type="text/javascript"></script>
    <script src="./_Feature Detection_files/index.js.download" type="text/javascript"></script>
    <script src="./_Feature Detection_files/require.js.download" type="text/javascript" charset="utf-8"></script>
    <script>
      require.config({
          
          urlArgs: "v=20210519195250",
          
          baseUrl: '/static/',
          paths: {
            'auth/js/main': 'auth/js/main.min',
            custom : '/custom',
            nbextensions : '/nbextensions',
            kernelspecs : '/kernelspecs',
            underscore : 'components/underscore/underscore-min',
            backbone : 'components/backbone/backbone-min',
            jed: 'components/jed/jed',
            jquery: 'components/jquery/jquery.min',
            json: 'components/requirejs-plugins/src/json',
            text: 'components/requirejs-text/text',
            bootstrap: 'components/bootstrap/dist/js/bootstrap.min',
            bootstraptour: 'components/bootstrap-tour/build/js/bootstrap-tour.min',
            'jquery-ui': 'components/jquery-ui/jquery-ui.min',
            moment: 'components/moment/min/moment-with-locales',
            codemirror: 'components/codemirror',
            termjs: 'components/xterm.js/xterm',
            typeahead: 'components/jquery-typeahead/dist/jquery.typeahead.min',
          },
          map: { // for backward compatibility
              "*": {
                  "jqueryui": "jquery-ui",
              }
          },
          shim: {
            typeahead: {
              deps: ["jquery"],
              exports: "typeahead"
            },
            underscore: {
              exports: '_'
            },
            backbone: {
              deps: ["underscore", "jquery"],
              exports: "Backbone"
            },
            bootstrap: {
              deps: ["jquery"],
              exports: "bootstrap"
            },
            bootstraptour: {
              deps: ["bootstrap"],
              exports: "Tour"
            },
            "jquery-ui": {
              deps: ["jquery"],
              exports: "$"
            }
          },
          waitSeconds: 30,
      });

      require.config({
          map: {
              '*':{
                'contents': 'services/contents',
              }
          }
      });

      // error-catching custom.js shim.
      define("custom", function (require, exports, module) {
          try {
              var custom = require('custom/custom');
              console.debug('loaded custom.js');
              return custom;
          } catch (e) {
              console.error("error loading custom.js", e);
              return {};
          }
      })

    document.nbjs_translations = {"domain": "nbjs", "locale_data": {"nbjs": {"": {"domain": "nbjs"}}}};
    document.documentElement.lang = navigator.language.toLowerCase();
    </script>

    
    

<script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="services/contents" src="./_Feature Detection_files/contents.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="custom/custom" src="./_Feature Detection_files/custom.js.download"></script><script type="text/javascript" charset="utf-8" async="" data-requirecontext="_" data-requiremodule="codemirror/mode/python/python" src="./_Feature Detection_files/python.js.download"></script></head>

<body class="edit_app" data-base-url="/" data-file-path="PycharmProjects/Augmented%20Reality/Feature%20Detection.py" data-jupyter-api-token="c15d9e2da5d4c775ab0417f55a8d59655c197c18de4c5afb" dir="ltr">

<noscript>
    <div id='noscript'>
      Jupyter Notebook requires JavaScript.<br>
      Please enable it to proceed. 
  </div>
</noscript>

<div id="header" role="navigation" aria-label="Top Menu" style="display: block;">
  <div id="header-container" class="container">
  <div id="ipython_notebook" class="nav navbar-brand"><a href="http://localhost:8888/tree?token=c15d9e2da5d4c775ab0417f55a8d59655c197c18de4c5afb" title="dashboard">
      <img src="./_Feature Detection_files/logo.png" alt="Jupyter Notebook">
  </a></div>

  

<span id="save_widget" class="pull-left save_widget">
    <span class="filename">Feature Detection.py</span>
    <div class="dirty-indicator-dirty" title="Unsaved changes"></div><span class="last_modified" title="Thu, May 20, 2021 4:39 PM">an hour ago</span>
</span>


  

  
  
  
  

    <span id="login_widget">
      
        <button id="logout" class="btn btn-sm navbar-btn">Logout</button>
      
    </span>

  

  
  
  </div>
  <div class="header-bar"></div>

  

<div id="menubar-container" class="container">
  <div id="menubar">
    <div id="menus" class="navbar navbar-default" role="navigation">
      <div class="container-fluid">
          <p class="navbar-text indicator_area">
          <span id="current-mode" title="The current language is Python">Python</span>
          </p>
        <button type="button" class="btn btn-default navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
          <i class="fa fa-bars"></i>
          <span class="navbar-text">Menu</span>
        </button>
        <ul class="nav navbar-nav navbar-right">
          <li id="notification_area"><div id="notification_save" class="notification_widget btn btn-xs navbar-btn" style="display: none;"><span></span></div></li>
        </ul>
        <div class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li class="dropdown"><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" class="dropdown-toggle" data-toggle="dropdown" aria-expanded="false">File</a>
              <ul id="file-menu" class="dropdown-menu">
                <li id="new-file"><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#">New</a></li>
                <li id="save-file"><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#">Save</a></li>
                <li id="rename-file"><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#">Rename</a></li>
                <li id="download-file"><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#">Download</a></li>
              </ul>
            </li>
            <li class="dropdown"><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" class="dropdown-toggle" data-toggle="dropdown">Edit</a>
              <ul id="edit-menu" class="dropdown-menu">
                <li id="menu-find"><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#">Find</a></li>
                <li id="menu-replace"><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#">Find &amp; Replace</a></li>
                <li class="divider"></li>
                <li class="dropdown-header">Key Map</li>
                <li id="menu-keymap-default" class="selected-keymap"><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#">Default<i class="fa"></i></a></li>
                <li id="menu-keymap-sublime"><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#">Sublime Text<i class="fa"></i></a></li>
                <li id="menu-keymap-vim"><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#">Vim<i class="fa"></i></a></li>
                <li id="menu-keymap-emacs"><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#">emacs<i class="fa"></i></a></li>
              </ul>
            </li>
            <li class="dropdown"><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" class="dropdown-toggle" data-toggle="dropdown">View</a>
              <ul id="view-menu" class="dropdown-menu">
              <li id="toggle_header" title="Show/Hide the logo and notebook title (above menu bar)">
              <a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#">Toggle Header</a></li>
              <li id="menu-line-numbers"><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#">Toggle Line Numbers</a></li>
              </ul>
            </li>
            <li class="dropdown"><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" class="dropdown-toggle" data-toggle="dropdown">Language</a>
              <ul id="mode-menu" class="dropdown-menu">
              <li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to APL">APL</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to PGP">PGP</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to ASN.1">ASN.1</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Asterisk">Asterisk</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Brainfuck">Brainfuck</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to C">C</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to C++">C++</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Cobol">Cobol</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to C#">C#</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Clojure">Clojure</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to ClojureScript">ClojureScript</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Closure Stylesheets (GSS)">Closure Stylesheets (GSS)</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to CMake">CMake</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to CoffeeScript">CoffeeScript</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Common Lisp">Common Lisp</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Cypher">Cypher</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Cython">Cython</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Crystal">Crystal</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to CSS">CSS</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to CQL">CQL</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to D">D</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Dart">Dart</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to diff">diff</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Django">Django</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Dockerfile">Dockerfile</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to DTD">DTD</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Dylan">Dylan</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to EBNF">EBNF</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to ECL">ECL</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to edn">edn</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Eiffel">Eiffel</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Elm">Elm</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Embedded Javascript">Embedded Javascript</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Embedded Ruby">Embedded Ruby</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Erlang">Erlang</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Esper">Esper</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Factor">Factor</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to FCL">FCL</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Forth">Forth</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Fortran">Fortran</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to F#">F#</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Gas">Gas</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Gherkin">Gherkin</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to GitHub Flavored Markdown">GitHub Flavored Markdown</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Go">Go</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Groovy">Groovy</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to HAML">HAML</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Haskell">Haskell</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Haskell (Literate)">Haskell (Literate)</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Haxe">Haxe</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to HXML">HXML</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to ASP.NET">ASP.NET</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to HTML">HTML</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to HTTP">HTTP</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to IDL">IDL</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Pug">Pug</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Java">Java</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Java Server Pages">Java Server Pages</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to JavaScript">JavaScript</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to JSON">JSON</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to JSON-LD">JSON-LD</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to JSX">JSX</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Jinja2">Jinja2</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Julia">Julia</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Kotlin">Kotlin</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to LESS">LESS</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to LiveScript">LiveScript</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Lua">Lua</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Markdown">Markdown</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to mIRC">mIRC</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to MariaDB SQL">MariaDB SQL</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Mathematica">Mathematica</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Modelica">Modelica</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to MUMPS">MUMPS</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to MS SQL">MS SQL</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to mbox">mbox</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to MySQL">MySQL</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Nginx">Nginx</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to NSIS">NSIS</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to NTriples">NTriples</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Objective-C">Objective-C</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to OCaml">OCaml</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Octave">Octave</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Oz">Oz</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Pascal">Pascal</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to PEG.js">PEG.js</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Perl">Perl</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to PHP">PHP</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Pig">Pig</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Plain Text">Plain Text</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to PLSQL">PLSQL</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to PostgreSQL">PostgreSQL</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to PowerShell">PowerShell</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Properties files">Properties files</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to ProtoBuf">ProtoBuf</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Python">Python</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Puppet">Puppet</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Q">Q</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to R">R</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to reStructuredText">reStructuredText</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to RPM Changes">RPM Changes</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to RPM Spec">RPM Spec</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Ruby">Ruby</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Rust">Rust</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to SAS">SAS</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Sass">Sass</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Scala">Scala</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Scheme">Scheme</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to SCSS">SCSS</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Shell">Shell</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Sieve">Sieve</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Slim">Slim</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Smalltalk">Smalltalk</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Smarty">Smarty</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Solr">Solr</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to SML">SML</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Soy">Soy</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to SPARQL">SPARQL</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Spreadsheet">Spreadsheet</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to SQL">SQL</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to SQLite">SQLite</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Squirrel">Squirrel</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Stylus">Stylus</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Swift">Swift</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to sTeX">sTeX</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to LaTeX">LaTeX</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to SystemVerilog">SystemVerilog</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Tcl">Tcl</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Textile">Textile</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to TiddlyWiki ">TiddlyWiki </a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Tiki wiki">Tiki wiki</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to TOML">TOML</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Tornado">Tornado</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to troff">troff</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to TTCN">TTCN</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to TTCN_CFG">TTCN_CFG</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Turtle">Turtle</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to TypeScript">TypeScript</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to TypeScript-JSX">TypeScript-JSX</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Twig">Twig</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Web IDL">Web IDL</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to VB.NET">VB.NET</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to VBScript">VBScript</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Velocity">Velocity</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Verilog">Verilog</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to VHDL">VHDL</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Vue.js Component">Vue.js Component</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to XML">XML</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to XQuery">XQuery</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Yacas">Yacas</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to YAML">YAML</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to Z80">Z80</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to mscgen">mscgen</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to xu">xu</a></li><li><a href="http://localhost:8888/edit/PycharmProjects/Augmented%20Reality/Feature%20Detection.py#" title="Set language to msgenny">msgenny</a></li></ul>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="lower-header-bar"></div>


</div>

<div id="site" style="display: block; height: 478px;">


<div id="texteditor-backdrop">
<div id="texteditor-container" class="container"><div class="CodeMirror cm-s-ipython CodeMirror-wrap" style="height: 438px;"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 428px; left: 530.646px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;"></textarea></div><div class="CodeMirror-vscrollbar" tabindex="-1" cm-not-content="true" style="display: block; bottom: 0px;"><div style="min-width: 1px; height: 1078px;"></div></div><div class="CodeMirror-hscrollbar" tabindex="-1" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1" draggable="false"><div class="CodeMirror-sizer" style="margin-left: 34px; margin-bottom: -17px; border-right-width: 13px; min-height: 1078px; padding-right: 17px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre class="CodeMirror-line-like">x</pre></div><div class="CodeMirror-measure"><pre class="CodeMirror-line" role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">cv2</span>.<span class="cm-property">imshow</span>(<span class="cm-string">'Result'</span>, <span class="cm-variable">img3</span>) &nbsp; &nbsp; &nbsp;<span class="cm-comment"># final good matches visualized </span></span></pre></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style="visibility: hidden;"></div><div class="CodeMirror-code" role="presentation" style=""><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">1</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string">"""</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">2</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string">Image features are unique parts of an image that help defining it. In other words these are specific patterns or specific features which are  unique, can be easily tracked and can be easily compared.</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">3</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string">For example in a scenery, an image patch of the sky would be difficult to identify since its spread over a lot of area</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">4</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string">but to identify an image patch containing the top of pine cone tree is easier thus making it a better feature. </span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">5</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string">"""</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">6</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">7</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">cv2</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">8</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">numpy</span> <span class="cm-keyword">as</span> <span class="cm-variable">np</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">9</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">import</span> <span class="cm-variable">utils</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">10</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">11</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">img1</span> <span class="cm-operator">=</span> <span class="cm-variable">cv2</span>.<span class="cm-property">imread</span>(<span class="cm-string">'C:/Users/Sakshee/Pictures/query.jpg'</span>, <span class="cm-number">0</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">12</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">img2</span> <span class="cm-operator">=</span> <span class="cm-variable">cv2</span>.<span class="cm-property">imread</span>(<span class="cm-string">'C:/Users/Sakshee/Pictures/train.jpg'</span>, <span class="cm-number">0</span>) &nbsp; <span class="cm-comment"># an image similar to img1 but at a different warped angle</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">13</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">14</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-comment"># ORB detector: Oriented FAST and Rotated BRIEF</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">15</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">orb</span> <span class="cm-operator">=</span> <span class="cm-variable">cv2</span>.<span class="cm-property">ORB_create</span>(<span class="cm-variable">nfeatures</span><span class="cm-operator">=</span><span class="cm-number">1000</span>) &nbsp; &nbsp; &nbsp;<span class="cm-comment"># default value = 500</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">16</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">17</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string">""" </span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">18</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string">Keypoint 1(kp1) and descripter 1(des1)</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">19</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string">The detector will find keypoints which are unique to the image and mark them descripters are an array or bin of numbers with a shape of (1000, 32) since we are using nfeatures = 1000</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">20</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string"># and for each feature tries to describe it in 32 values </span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">21</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string">"""</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">22</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">23</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">kp1</span>, <span class="cm-variable">des1</span> <span class="cm-operator">=</span> <span class="cm-variable">orb</span>.<span class="cm-property">detectAndCompute</span>(<span class="cm-variable">img1</span>, <span class="cm-keyword">None</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">24</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">kp2</span>, <span class="cm-variable">des2</span> <span class="cm-operator">=</span> <span class="cm-variable">orb</span>.<span class="cm-property">detectAndCompute</span>(<span class="cm-variable">img2</span>, <span class="cm-keyword">None</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">25</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-builtin">print</span>(<span class="cm-variable">kp1</span>) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span class="cm-comment"># type = list</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">26</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-builtin">print</span>(<span class="cm-builtin">len</span>(<span class="cm-variable">kp1</span>)) &nbsp; &nbsp; &nbsp; &nbsp;<span class="cm-comment"># since we have set nfeatures to 1000 it will find 1000 keypoints</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">27</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-builtin">print</span>(<span class="cm-variable">des1</span>.<span class="cm-property">shape</span>) &nbsp; &nbsp; &nbsp;<span class="cm-comment"># each key point is described by 32 calues</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">28</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">29</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">imgKp1</span> <span class="cm-operator">=</span> <span class="cm-variable">cv2</span>.<span class="cm-property">drawKeypoints</span>(<span class="cm-variable">img1</span>, <span class="cm-variable">kp1</span>, <span class="cm-keyword">None</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">30</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">imgKp2</span> <span class="cm-operator">=</span> <span class="cm-variable">cv2</span>.<span class="cm-property">drawKeypoints</span>(<span class="cm-variable">img2</span>, <span class="cm-variable">kp2</span>, <span class="cm-keyword">None</span>)</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">31</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">32</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string">"""</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -34px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">33</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-string">No we will try to match the descriptors obtained from the two images to check how similar they are. We use BFMatcher.knnMatch() to get the k best matches.</span></span></pre></div></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 1078px;"></div><div class="CodeMirror-gutters" style="height: 1091px; left: 0px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 33px;"></div></div></div></div></div>
</div>


</div>






    


<script src="./_Feature Detection_files/main.min.js.download" type="text/javascript" charset="utf-8"></script>


<script type="text/javascript">
  function _remove_token_from_url() {
    if (window.location.search.length <= 1) {
      return;
    }
    var search_parameters = window.location.search.slice(1).split('&');
    for (var i = 0; i < search_parameters.length; i++) {
      if (search_parameters[i].split('=')[0] === 'token') {
        // remote token from search parameters
        search_parameters.splice(i, 1);
        var new_search = '';
        if (search_parameters.length) {
          new_search = '?' + search_parameters.join('&');
        }
        var new_url = window.location.origin + 
                      window.location.pathname + 
                      new_search + 
                      window.location.hash;
        window.history.replaceState({}, "", new_url);
        return;
      }
    }
  }
  _remove_token_from_url();
</script>


</body></html>