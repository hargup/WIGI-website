A skeleton of the website intended to display interactive graphs statistically
quantifying the gender gap in Wikipedia biographies, through several
indicators.

The project was conceived by Max Klein (https://notconfusing.com) and is
[funded](https://meta.wikimedia.org/wiki/Grants:IdeaLab/WIGI:_Wikipedia_Gender_Index)
by Wikimedia organization through an [individual engagement
grant](https://meta.wikimedia.org/wiki/Grants:IEG). Development is continued by
a Max himself and a voluntarily assembled team of researchers, developers and
designers.

Read the complete [prototype research](http://arxiv.org/abs/1502.03086) and
[preliminary
results](http://notconfusing.com/preliminary-results-from-wigi-the-wikipedia-gender-inequality-index/).

Design
======

The website is based on popularly used Python based static site generator,
[Nikola](http://getnikola.com). After post processing of Wikidata, graphs are
generated using [Bokeh](http://bokeh.pydata.org/en/latest/), another Python
based interactive visualization library targeting web browsers.

We currently intend to display four graphs: Gender by Culture, Gender by
Country (World Map), Gender by Date of Birth, and Wikipedia Language by Gender.

Run it locally
==============

To run the website locally, ensure that you have installed latest version of
Nikola and Bokeh. We recommended to use [conda](http://conda.pydata.org/docs/),
which is an open source python package and environment management tool. The
installation instructions can be found on their respective websites. Once the
dependencies are installed, run the following set of commands:

```
git clone https://github.com/hargup/WIGI-website
cd WIGI-website
nikola build && nikola serve
```

If everything goes fine, you should be able to see WIGI website at
127.0.0.1:8000.

Please note that you need use the Nikola provided server to serve the requests.
The output of `nikola build` is a self contained, static website in the
`output/` directory, which can be rendered by any server. A [quick python
server](https://docs.python.org/3.5/library/http.server.html), for example.

How does it work?
=================

All you need to know for running the WIGI website and playing with graphs is to
run `nikola build && nikola serve`. If, however, you want to add more graphs or
play with new data, there are couple of things to note.

It all starts with the `conf.py` file in the repository root directory. This
file is used to configure how Nikola behaves and how does it generate static
HTML pages from templates.

1. All the posts are constructed from their specific templates, which file
   metadata and instructions on how to render the specific HTML page. For
example, `gender by country.md` post has the following one line in the
description:

```
.. template: gender_by_country.tmpl
```

This specifies the template to be used for creating the `gender_by_country.html`
file. The templates are located in `templates/` directory.

2. Templates instruct how to build web page and where to embed Bokeh graph. For
   example, if you open `gender_by_country.tmpl` for example, you can find the
following block
```
<%block name="plot">
    ${gender_by_country_plot}
</%block>
```
which embeds the plot data (through `gender_by_country` plot) within the `plot`
block of the HTML page and renders it further.

3. The interesting part, as to how Nikola templates receive the plot data, can
  be answered by inspecting `conf.py`. When `nikola build` is run, first
`conf.py` is executed. In this file, we import our Bokeh plot generating
functions and generate respective plots' data. These data are then made
available to all the Nikola templates by putting them into `GLOBAL_CONTEXT`.

```
GLOBAL_CONTEXT = {
        "gender_by_country_plot": gender_by_country.plot(),
        "gender_by_culture_plot": gender_by_culture.plot(),
        "gender_by_dob_plot": gender_by_dob.plot(),
        "language_by_gender_plot": language_by_gender.plot()
    }
```

These variables were referenced in the respective template files (as explained
in point 2) to embed the plot data.

All of this happens automatically by running `nikola build`.

Adding a plot
=============

If you have a new plot to add, you need to add the following files:

1. A Python script to generate the Bokeh plot data and import the function in
   `conf.py`. Place the script in `plots/` directory and see any existing file
to learn about what the function should do and return.
2. A template file `<graph>.tmpl` describing where you want to embed the plot
   data.
3. A markdown file `<post>.md` referencing the template in the description, and
   other data (text, commentary, citations etc.,) you want along with the post.

Please see any existing file for clear example. Once you are done, run `nikola
build && nikola serve`.

Using new data
==============

All the data used by Bokeh scripts can be found in `data/` directory in
repository root. If you want to use new data, update the respective csv files
with suitable data. It is recommended to keep new data files in this directory
only.

Contributors
============

Max Klein (@notconfusing), Vivek Rai (@vivekiitkgp), Harsh Gupta (@hargup)

License
=======

All source code files and content are available under MIT License and content
is available under a [Creative Commons Attribution-ShareAlike 4.0 International
License](http://creativecommons.org/licenses/by-sa/4.0/) respectively.
