[![Build Status](https://travis-ci.org/hargup/WIGI-website.svg)](https://travis-ci.org/hargup/WIGI-website)

-------------------

WIGI is a project producing a <strong>open data set</strong> about the
*gender, date of birth, place of birth, ethnicity, occupation*, and *language*
of **biography articles** in all Wikipedias. Our [data
set](http://wigi.wmflabs.org/snapshot_data/) comes from
[Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page), the database the
feeds Wikipedia, and is updated weekly. This website shows a few demonstrations
of what can be done with that information.


This project started as a [personal research
interest](http://arxiv.org/abs/1502.03086), and is now [funded by a Wikimedia
Foundation
Grant](https://meta.wikimedia.org/wiki/Grants:IEG/WIGI:_Wikipedia_Gender_Index).

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

Getting the data
----------------

To run the site offline, you must download a set `newest` and `newest-changes`
snapshot data from the server. A tar file containing these latest changes is
available at [snapshot data](http://wigi.wmflabs.org/snapshot_data).

Please download and extract at a convenient location.


Running the site
----------------

We recommended installing [conda](http://conda.pydata.org/miniconda.html), an
open source python package and environment management tool. The installation
instructions can be found on their respective websites. **Please install the
Python 3 version or create a Python 3 environment as current setup supports
only Python 3.**

Once you have cloned the repository, run the following command inside the
directory to install dependencies:

```
pip install -r requirements.txt
```

In case `pip` is missing, run `conda install pip`. Once the installation is
complete (might take a while), next step is to configure the location to your
data directory.

Open `config.py.sample` inside the `plots/` folder and edit the `data_dir` path
to the location where you extracted `snapshot_data` in previous step. Rename
the file to `config.py` or create a new one if you wish.

Finally, run:

```
nikola build && nikola serve
```

If everything goes fine, you should be able to see WIGI website in action at
[127.0.0.1:8000](http://127.0.0.1:8000).

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
following block which embeds the plot data (using a `plot_helper.tmpl` template
file) on the page and renders it.


```
${plot.changes('gender_by_country')}
${plot.alltime('gender_by_country')}
```

3. The interesting part, as to how Nikola templates receive the plot data, can
   be answered by inspecting `conf.py`. When `nikola build` is run, first
`conf.py` is executed. In this file, we import our Bokeh plot generating
functions and generate respective plots' data. These data are then made
available to all the Nikola templates as a `plots` dictionary by putting them
into `GLOBAL_CONTEXT`.

```
GLOBAL_CONTEXT = {
    'plots' : {
        'gender_by_country': {
            'newest': gender_by_country.plot('newest'),
            'newest_changes': gender_by_country.plot('newest-changes')
            },
        'gender_by_culture': {
            'newest': gender_by_culture.plot('newest'),
            'newest_changes': gender_by_culture.plot('newest-changes')
            },
        ...
    }
```

    These variables were referenced in the respective template files (as
explained in point (2) to embed the plot data.

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

Just add any updated data to the `data_dir` you have used in the `config.py`
file, and let your script use it.

Contributors
============

Max Klein (@notconfusing), Vivek Rai (@raivivek), Harsh Gupta (@hargup)

Questions?
==========

WHGI [Google Group](https://groups.google.com/forum/#!forum/wigi-project) is the
best way to reach to us and community of users who have used WHGI.
Alternatively, feel free to reach out to corresponding authors via email.

Citation
========

```
@inproceedings{Klein:2016:MGG:2957792.2957798,
 author = {Klein, Maximilian and Gupta, Harsh and Rai, Vivek and Konieczny, Piotr and Zhu, Haiyi},
 title = {Monitoring the Gender Gap with Wikidata Human Gender Indicators},
 booktitle = {Proceedings of the 12th International Symposium on Open Collaboration},
 series = {OpenSym '16},
 year = {2016},
 isbn = {978-1-4503-4451-7},
 location = {Berlin, Germany},
 pages = {16:1--16:9},
 articleno = {16},
 numpages = {9},
 url = {http://doi.acm.org/10.1145/2957792.2957798},
 doi = {10.1145/2957792.2957798},
 acmid = {2957798},
 publisher = {ACM},
 address = {New York, NY, USA},
 keywords = {Biographical Database, Gender Disparities, Wikidata, Wikipedia},
}
```

License
=======

All source code files are available under MIT License and content is available
under a [Creative Commons Attribution-ShareAlike 4.0 International
License](http://creativecommons.org/licenses/by-sa/4.0/) respectively.
