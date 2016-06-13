
3.23
 - Got github
 - Got xlwings
     - http://docs.xlwings.org/installation.html
     - need to get pywin32, here: http://sourceforge.net/projects/pywin32/postdownload?source=dlp
     - learn here: http://xlwings.org/quickstart/

 - Random articles

  Git aliases (combined commands)
  http://haacked.com/archive/2014/07/28/github-flow-aliases/
     
  Guy at UWisconsin, maintains Git for Windows + does BioImaging
  http://loci.wisc.edu/people/johannes-schindelin
  
  Good VB walkthru
  https://msdn.microsoft.com/en-us/library/9a4y3z34.aspx
  
  C# vs C++ in performance
  http://stackoverflow.com/questions/4257659/c-sharp-versus-c-performance
  
  OpenCV + .NET
  http://www.emgu.com/wiki/index.php/Main_Page
  
      getting the compiled thing on rpi
      https://spacerazor.wordpress.com/2014/08/28/emgucv-on-the-raspberry-pi-with-mono/
      
      using the camera-board instead of usb webcam
          https://spacerazor.wordpress.com/2014/08/30/emgucv-with-the-raspberry-pi-camera-module/ 
  
          https://www.youtube.com/watch?v=MWK55A0RH0U&feature=youtu.be
          
          https://github.com/neutmute/robidouille/tree/master/raspicam_cv
		  
3.24


 - Random Articles
 
  Python 10 myths
  https://www.paypal-engineering.com/2014/12/10/10-myths-of-enterprise-python/
  https://news.ycombinator.com/item?id=9256082
  
  Python performance with Intel MathKit vs. Atlas for Linear Algebra
  https://software.intel.com/en-us/articles/numpyscipy-with-intel-mkl
  
  PyCharm IDE
  https://www.jetbrains.com/pycharm/
  
  Norvig Spell Checker
  http://norvig.com/spell-correct.html
  
  Crowd sourcing dev help
  http://crowdcrafting.org/
  
  Python Global Interpreter Lock
  https://wiki.python.org/moin/GlobalInterpreterLock
  

3.25
  
  Rpi + OpenCV: look in comments for other ways to build, claims 32 fps for tracking
  http://www.pyimagesearch.com/2015/02/23/install-opencv-and-python-on-your-raspberry-pi-2-and-b/
  
  Git Tut from Recurse Center
  https://codewords.recurse.com/issues/two/git-from-the-inside-out
  
 3.27
 
  HN Algo
  http://amix.dk/blog/post/19574
  
  Rails is a Ghetto, Zed Shaw
  http://harmful.cat-v.org/software/ruby/rails/is-a-ghetto
  
  Learn X in Y minutes, nice cheat sheet
  http://learnxinyminutes.com/docs/python/
  http://learnxinyminutes.com/docs/git/
  
  Parsing ls
  http://mywiki.wooledge.org/ParsingLs
  
  cd to a directory #x with bash script
  a=($(ls))
  b=cd" "${a[x]}
  $b
  
  
  finding ways to break on value change
  http://stackoverflow.com/questions/160045/break-when-a-value-changes-using-the-visual-studio-debugger
  
  Visual Commander - 3rd party alternate to Macros in VisualStudios
  https://vlasovstudio.com/visual-commander/
  
  sqlite plugin for VS
  http://sqlcetoolbox.codeplex.com/documentation
  http://sqlcetoolbox.codeplex.com/license
  
 
 3.30
 
   To use command window in VS, > Tools.shell /commandwindow c:/..../app.exe
   https://msdn.microsoft.com/en-us/library/0xca6kdd.aspx
 
   vb.net: To split file by lines
   Dim split4 As String() = global_file.Split(New String() {Environment.NewLine}, StringSplitOptions.None)
   
   VB list structures
   Imports System.Collections.ArrayList
   Imports System.Collections.Generic
  
 3.31
 
    When VBA doesn't run anything for no reason, goto VBA IDE > View > ErrorList, fix errors, boom.
	
 4.1

   discussion of .net for opencv
   http://stackoverflow.com/questions/85569/net-dotnet-wrappers-for-opencv
   
   sports analytics, basketball
   http://www.secondspectrum.com/	
   
   I2C and SPI writeup
   http://www.byteparadigm.com/applications/introduction-to-i2c-and-spi-protocols/
   
   Rpi to arduino
   http://blog.oscarliang.net/raspberry-pi-arduino-connected-i2c/
   http://www.instructables.com/id/Raspberry-Pi-I2C-Python/
   
   Interesting engineer's blog, doing IoT things, Heroku / Saleforce
   http://reidcarlberg.com/
   https://github.com/ReidCarlberg
   
   Rule #1: do what adafruit says
   https://learn.adafruit.com/using-the-bmp085-with-raspberry-pi/configuring-the-pi-for-i2c 
   
4.2		

   ShortcutKey DB
   http://www.veodin.com/keyrocket/shortcut-database/
		for VS2012
		http://www.veodin.com/keyrocket/visual-studio-2012-shortcuts/
   
   How non-developers can contribute to open-source projects discussion
   https://news.ycombinator.com/item?id=9307255
   
   
 4.3
 
   Functional Programming
   
      Described for python
	  https://docs.python.org/2/howto/functional.html#passing-values-into-a-generator
		
		itertools
		https://docs.python.org/2/library/itertools.html#module-itertools
	  
	  Examples for VB
	  https://msdn.microsoft.com/en-us/library/orm-9780596518431-01-09.aspx
	  
	SeatGeek - tickets
	http://blogs.wsj.com/venturecapital/2015/04/02/seatgeek-scores-62-million-for-its-ticket-selling-app/
	https://news.ycombinator.com/item?id=9313898
	
	Freeman Dyson, Scientist as rebel	https://books. .com/books?id=Jhr8AwAAQBAJ&lpg=PT15&ots=MreY2f8eEg&dq=scientist%20as%20a%20rebel&pg=PT15#v=onepage&q&f=falsehttps://books.google.com/books?id=Jhr8AwAAQBAJ&lpg=PT15&ots=MreY2f8eEg&dq=scientist%20as%20a%20rebel&pg=PT15#v=onepage&q&f=false
	
	Verizon headers
	https://news.ycombinator.com/item?id=8500131
	
 4.6
 
   Get this: VS Aync CTP v3
    http://www.microsoft.com/en-us/download/details.aspx?id=9983
	
  4.7
  
    Rpi GPIO for .net
	https://pisharp.codeplex.com/
	
	Call Cpp with Csharp vis-avis CppSharp
	https://github.com/mono/CppSharp
	
  4.8
  
     Micromanipulator / Dissector
	 https://backyardbrains.com/products/micromanipulator
	 
	 Days of War
	 http://www.crimethinc.com/books/days.html
	 
	 Info addiction book
	 http://www.amazon.com/The-Distraction-Addiction-Information-Communication/dp/0316208264
	 
  4.10
  
     OpenSource .net Libraries
	 http://thomasvm.github.io/blog/2015/03/17/open-source-net-libraries-that-make-your-life-easier/
	 https://news.ycombinator.com/item?id=9353668
	 https://github.com/tallesl/.NET-libraries
	 
	 Another .net guy
	 http://www.hanselman.com/blog/HowToRunBackgroundTasksInASPNET.aspx
   
     Helpful python import/loading modules question http://stackoverflow.com/questions/3061/calling-a-function-of-a-module-from-a-string-with-the-functions-name-in-python?rq=1
	 
	 python __del__()  / GC / teardown, etc
	 http://stackoverflow.com/questions/1339293/python-memory-leak-debugging
	 http://stackoverflow.com/questions/11891755/find-all-references-to-an-object-in-python/11891904#1189190http://stackoverflow.com/questions/11891755/find-all-references-to-an-object-in-python/11891904#11891904
	 http://stackoverflow.com/questions/16686788/python-how-to-kill-a-class-instance-object
	 http://nedbatchelder.com/blog/200809/a_server_memory_leak.html
	 
     
   4.14
   
   C# Exceptions
   http://www.volatileread.com/Wiki?id=1087
   
   F# Discussion and Poll
   https://news.ycombinator.com/item?id=9373269
   
		Tutorial for F#
		http://fsharp.org/about/learning.html
		
		MSTutorial - functional Prgoramming
		https://msdn.microsoft.com/en-us/library/vstudio/hh314518%28v=vs.100%29.aspx
		
		Community Watercoolers
		https://sergeytihon.wordpress.com/category/f-weekly/
		http://blogs.msdn.com/b/fsharpteam/
		http://www.tryfsharp.org/
   
    
	Python PIL - Imaging Factory
	http://effbot.org/imagingbook/image.htm
	
	Pip for .Net
	https://www.nuget.org/packages/NuGet.CommandLine/
   
   Python exception handling
   
	   import zmq
	   http://zguide.zeromq.org/py:interrupt
   
		python frames
		http://stackoverflow.com/questions/1140194/in-python-how-do-i-obtain-the-current-frame
		
		register a function atexit
		https://docs.python.org/2/library/atexit.html#module-atexit
		
		python signal, for asnyc proc communication
		https://docs.python.org/2/library/signal.html#example
		
		
   4.15
   
   Self-Host Sci Journal with e-lens
   https://medium.com/@_mql/self-host-a-scientific-journal-with-elife-lens-f420afb678aa
   
   4.16
   
   Serving Tiles in Go
   https://http2.golang.org/gophertiles?latency=0
   https://news.ycombinator.com/item?id=9388325
   
   Interesting blog
   https://nydwracu.wordpress.com/
   http://tendrilsofreality.tumblr.com/
   
   4.17
   
   Prompts for programmers
   http://kevinlawler.com/prompts
   
   4.21
   
   Regular Expressions for .Net
   https://msdn.microsoft.com/en-us/library/2k3te2cs.aspx
   
   4.22
   Python books - cools stuff
   http://automatetheboringstuff.com/
   http://inventwithpython.com/
   
   Enferno: A template for using Flask as lightweight swiss-army knife
   http://enferno.io/
		
		a write-up blog
     	https://medium.com/project-enferno/create-your-first-minion-with-project-enferno-f7884aa95443
   
		the dude
		https://news.ycombinator.com/user?id=level09, 
   
   
    4.23
	
	H/N Strat's 
    http://antontarasenko.com/2015/04/23/best-time-to-post-its-irrelevant/	http://nbviewer.ipython.org/github/antontarasenko/blog-replication-files/blob/master/2015/hacker_news_timing/hn_posting_time.ipynb
	http://minimaxir.com/2014/02/hacking-hacker-news/
   
    C#7 RFC
	https://github.com/dotnet/roslyn/issues/2136
	
   
    4.24
	
	OpenCV  report from 2010
	http://codecapsule.com/2010/07/26/four-weeks-with-opencv/
	
	Periscope - SQL tool
	https://www.periscope.io/blog
	
	
	4.27
	
	https://docs.google.com/a/welis.com/spreadsheets/d/1swcl3PWGQHMyfdPG8k9uo05_oajGbXMin-Ou6VjZq14/edit#gid=0
	
	Prisoners Escape of chessboard / coins logic problem
	http://datagenetics.com/blog/december12014/index.html
	
	4.29
	
	PAckageMAnagement Windows10
	http://blogs.technet.com/b/packagemanagement/archive/2015/04/29/introducing-packagemanagement-in-windows-10.aspx
	
	Currently a good one
	https://chocolatey.org/
	
	Comparing ML languages
	http://thebreakfastpost.com/2015/04/22/four-mls-and-a-python/
	
	4.30
	
	MS goes off
		MS launches .NET for linux/mac
		https://news.ycombinator.com/item?id=9459513
		
		MS makes VisualStudios CrossPlatform
		https://news.ycombinator.com/item?id=9459364
		
		open sourcing c++ debugger	http://blogs.msdn.com/b/vcblog/archive/2015/04/29/open-sourcing-visual-studio-s-gdb-lldb-debug-engine.aspx
		
	
	postgres vs sqlserver
	http://www.pg-versus-ms.com/
	https://news.ycombinator.com/item?id=9464505
	
		CLR in SQLserver
		https://msdn.microsoft.com/en-us/library/ms131102(v=sql.110).aspx
	


	Maps
		serving tiles with postgres,apache,postgis, osm
		https://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/
		
		calvin's tile server, fractal map
		http://catilinejs.com/website/leaflet-fractal/#500/-0.37/0.6/julia
		
		Wiki on Tile Servers
		http://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#Tile_servers
	
		Slippy Map
		http://wiki.openstreetmap.org/wiki/Deploying_your_own_Slippy_Map
		
		C# (Client?) for slippy
		https://github.com/BruTile/BruTile
		
		Tile Drawer
		https://github.com/migurski/Tile-Drawer
	
	
	Rpi measure/explore ebook, $0?
	https://leanpub.com/b/theauthorbundle/
	
	
	5.1
	
	F# 4.0 Review
	http://www.infoq.com/news/2015/04/FSharp-4
	
	LabMinds, solution prep robot. Boston based
	 http://www.labminds.co/video/solution-preparation
	 
	
	5.4
	
	GPU parsing of csv
	https://github.com/antonmks/nvParse
	 
	VS regex
	https://msdn.microsoft.com/en-us/library/2k3te2cs.aspx
	 
	5.6
	
	Baseball Model
	http://footballcommentary.com/bbmodel.htm
	
	Money Mustache
	http://www.mrmoneymustache.com/
	
	5.12
	
	Libertarian Climate
	https://climateunplugged.com/blogpost/?postid=951
	
	5.13
	
	C# - wiki books
	http://en.wikibooks.org/wiki/C_Sharp_Programming/The_.NET_Framework/Threading
	
	5.14
	
	Image 2 Excel
	https://github.com/Dobiasd/img2xls
	
	Plain Text for Diagrams
	http://monodraw.helftone.com/
	
	5.15
	
	Breakthrough Institute - Return of Nature
	http://thebreakthrough.org/index.php/journal/issue-5/the-return-of-nature
	
	REST vs RPC
	http://apihandyman.io/do-you-really-know-why-you-prefer-rest-over-rpc/
	
	Code Projects - Canonical CS problems for any language
	https://github.com/karan/Projects
	
	Insurance Essay by Nick Szabo
	http://szabo.best.vwh.net/insurance.html
	
	5.20
	
	Async in Python
	https://lwn.net/SubscriberLink/643786/9c0bd83dff0df3b8/
	
	WCF Windows Comm Open Source
	http://www.dotnetfoundation.org/blog/wcf-is-open-source
	
	NuGET - PkgManager for .net
	http://www.nuget.org/
		VS > Tools > NuGet PAckage Manager Console
		
	Nancy - Flask for .net
	http://nancyfx.org/
	
	5.21
	
	Hadoop BAshing + Stucchio's an interesting dude
	https://www.chrisstucchio.com/blog/2013/hadoop_hatred.html
	
	5.22
	
	Holy Grail CSS Layout with Flexbox
	https://philipwalton.github.io/solved-by-flexbox/demos/holy-grail/
		
		flexbox demo - Bostock level designer
		http://bennettfeely.com/flexplorer/
		
	
	Front-End "Sandbox" / Github
	http://codepen.io/
	
	5.26
	
	Macros for python
	https://github.com/lihaoyi/macropy
		
	Bio + Imaging Guy on HN
	http://calculatedimages.blogspot.com/2015/04/light-years-of-dna.html
	
	
	5.28
	
	Tornado rail-esque starting guide by MIT bitcoin dev
	https://github.com/JeremyRubin/tornado-trails
		http://www.tornadoweb.org/en/stable/guide/intro.html
	
	https://medium.com/@moritzfelipe/why-bitcoin-should-replace-the-like-button-4fe1e1d38e7a
		
	5.29
	
	Github command line
	https://github.com/ingydotnet/git-hub
	
	
	6.2
	Alias in git bash - add .bashrc and source it
	
	http://superuser.com/questions/602872/how-do-i-modify-my-git-bash-profile-in-windows
	
	source command in bash
	http://ss64.com/bash/source.html
	
	6.4
	
	Karpathy on building chrome extensions
	http://karpathy.github.io/2013/11/23/chrome-extension-programming/
	
	
	6.5
	
	Abby @MozillaScienceLabs
	http://acabunoc.github.io/
	
	
	python xml tut
	http://pymotw.com/2/xml/etree/ElementTree/parse.html
	http://pymotw.com/2/Queue/index.html#module-Queue
	
	6.8
	
	GUI for python
	http://nucleic.github.io/enaml/docs/index.html
	
	6.9
	
	Ipython for emacs
	https://github.com/gregsexton/ob-ipython
	
	Meetup for Gingko dude 6/24
	http://www.meetup.com/Helbling-Visionary-Series/events/222825669/?eventId=222825669&action=detail 
	
	iGEM Meetup 6/19
	http://2015.igem.org/Meetups/New_England_(NEGEM)
	
	6.15
	
	Molecular programming
	http://molecular-programming.org/
	https://news.ycombinator.com/item?id=9717039
	
	6.17
	
	Commandline help
	https://github.com/jlevy/the-art-of-command-line
	
	"Datascience" command line
	http://datascienceatthecommandline.com/
	
	6.22
	
	DotNet Site
	http://www.dotnetrocks.com/
	
	KISS programming blog (21st century programming)
	http://prog21.dadgum.com/177.html
	
	Free Code Camp - they hep NonProfits
	http://www.wired.com/2015/06/can-real-world-work-free-coding-boot-camp/
	
	In 1870, 70-80 percent of the US population was employed in agriculture.[15] As of 2008, less than 2 percent of the population is directly employed in agriculture.[16][17]
	
	
	6.24
	
	Kayak: Canton to Milton
	http://bostonkayaker.com/cgi-bin/bkonekpage.cgi?pagekey=neponsetcanton
	
	
	6.25
	
	OCR Open source discussion
	https://news.ycombinator.com/item?id=9775753
	https://ocr.a9t9.com/
	
	OCR / Robotics blog
	http://blog.a9t9.com/
	
	6.30
	
	D3 Gallery of links
	https://github.com/wbkd/awesome-d3
	
	GNU PIC: box and arrow diagram software
	http://floppsie.comp.glam.ac.uk/Glamorgan/gaius/web/pic.html
	
	7.2
	Python Tut
	http://www.tutorialspoint.com/python/python_strings.htm
	
	Ipython + soduku + Flask from IBM	https://www.ibm.com/developerworks/community/blogs/jfp/entry/using_ipython_notebooks_in_docker_containers_on_windows?lang=en
	
	no-sql toy in python
	https://github.com/jeffknupp/nosql
	
	
	7.6
	
	Googel Neural Network "Dreams" Images
	http://gizmodo.com/googles-dream-robot-is-running-wild-across-the-internet-1715839224
	
	7.7
	
	Cindy Wu - on HN
	https://news.ycombinator.com/threads?id=cindywu123
		
	OpenBiotech Article
	http://sethbannon.com/biotech-in-the-garage
	
	Joan Didion - Self-Respect
	http://www.vogue.com/3241115/joan-didion-self-respect-essay-1961/
	
	Uncle Bob: Craftsman vs Laborer
	http://blog.8thlight.com/uncle-bob/2013/01/30/The-Craftsman-And-The-Laborer.html
	
	Explaining a Monad with F#
	http://fsharpforfunandprofit.com/posts/recipe-part2/
	
	7.9
	
	11-million-to-1 gearbox: microscope?
	http://makezine.com/2015/07/08/bet-cant-find-use-11-million-1-gearbox/
	https://news.ycombinator.com/item?id=9857025
	
	7.14
	
	LAuren Holliday - "Millenial Marketer" / Freelanship promoter
	https://www.linkedin.com/in/laurenaholliday
	
	7.15
	
	Chromecast Hacks
	http://readwrite.com/2013/07/30/chromecast-tips-tricks-workarounds-hacks-advice
	
		Blacker: http://forum.xda-developers.com/showthread.php?t=2382541
		
		Forgive my possible ignorance, but couldn't you just run a web server on your smb box and give the URL of your local vid stash?
		ie - pass http://192.168.1.10/public_html/vids/movie.mp4 to chromecast
	
		http://www.reddit.com/r/Chromecast/comments/1j8brm/hidden_settings_in_chromecasts_chrome_extension/cbcf5hy
		
	RPi - Media Center
	http://lifehacker.com/5929913/build-a-xbmc-media-center-with-a-35-raspberry-pi
	
	Funny Dancing guy
	https://www.facebook.com/LADbible/videos/2301572706556573/?fref=nf
	
	ImgProc Bio Guy
		https://github.com/luispedro
		http://luispedro.org/projects/datasets/
		Class on Cell segmentation	https://github.com/luispedro/python-image-tutorial/blob/907c2f975be836681bfc391041e3820e38fbafcb/Segmenting%20cell%20images%20(fluorescent%20microscopy%29.ipynb
	
	
	7.16
	
	VS2015 Release Event
	https://www.visualstudio.com/visualstudio-release-event-vs
	
	Python Code Bases
	https://news.ycombinator.com/item?id=9896369
	
	pip install from github
	http://www.reddit.com/r/Python/comments/2crput/how_to_install_with_pip_directly_from_github/
	
	7.17
	
	SO questions to answer
	https://stackoverflow.com/questions/26029592/insert-image-in-matplotlib-legend
	
	7.20
	
	Here's a bookmarklet you can use to enable zoom:	javascript:m=document.querySelector('meta%5Bname=viewport%5D');m.content=m.content.replace(/.*(width=%5B%5E,%5D+).*/,%22$1,maximum-scale=10,minimum-scale=0.1,user-scalable=1%22);
	I found it on HN a while ago, I wish i knew where. To add it bookmark another page then go into bookmarks edit mode and change the URL to that.
	
	VS2015 available for download	
	https://news.ycombinator.com/item?id=9916089	http://blogs.msdn.com/b/somasegar/archive/2015/07/20/visual-studio-2015-and-net-4-6-available-for-download.aspx
	
	Selenium implicits waits	http://stackoverflow.com/questions/31442119/mechanize-and-python-clicking-href-javascriptvoid0-links-and-getting-the
	
	VS Extensions blog
	http://www.visualstudioextensibility.com/category/vs14/
	
	7.21
	
	Poker class at MIT	http://ocw.mit.edu/courses/sloan-school-of-management/15-s50-poker-theory-and-analytics-january-iap-2015/index.htm
	
	Docker for Ipython
	https://github.com/jupyter/tmpnb

	TempNB - Temporary IPython site, for active branch for Jupyter project	https://tmp34.tmpnb.org/user/cA1oY79a3pOo/notebooks/featured/pandas-cookbook/cookbook/Chapter%204%20-%20Find%20out%20on%20which%20weekday%20people%20bike%20the%20most%20with%20groupby%20and%20aggregate.ipynb
	
	7.22
	
	Algorithmia blog - post on vote collusion
	http://blog.algorithmia.com/post/124542129914/mining-product-hunt-detecting-vote-rings
	
	Will write blog post on using Roslyn for CodeAnalysis
	https://news.ycombinator.com/user?id=JamesBarney
	
	Dakota's startup
	http://www.prospectiveresearch.com/
	
	Rpi cluster
	https://pocketcluster.wordpress.com/2015/07/23/raspberry-pi-2-cluster-case-pt2/
	
    
    7.22
    
    Ipython with .net https://github.com/ipython/ipython/wiki/Cookbook:-IPython-and-Python.NET
	
	7.26
    
   Visual Studio + Python

   scripting .net with ironpython http://www.codeproject.com/Articles/602112/Scripting-NET-Applications-with-IronPython
   
   OldSchool attempt at compiling to c# clr
   http://www.csscript.net/
   
   3 Minutes to using ironpython?
   http://www.secretgeek.net/host_ironpython
  
   Pyc.py is command line compiler for ironpython?http://stackoverflow.com/questions/1578010/ironpython-2-6-py-exe?lq=1
   
        which links to this example
        http://dbaportal.eu/2009/12/21/ironpython-how-to-compile-exe/
   
   
  Another tutorial http://ironpython.codeplex.com/wikipage?title=Samples&ProjectName=ironpython
   
   Chapter 1 for Free of "IronPython in Action"
   http://www.manning.com/foord/SampleChapter1.pdf
   
   VS is slow http://stackoverflow.com/questions/19617670/why-vs-2013-is-very-slow
	
   Simple StackO helloworld for .exe python
    http://stackoverflow.com/questions/14726803/creating-standalone-executable-iron-python-file
	
	Simple program 
    
        blog
        http://lifebeyondfife.com/79-ironpython-wpf-html/
        x
        source
        https://github.com/lifebeyondfife/IronPythonWPF
        
    Sweet, a pip install away from fucking compiling
    https://pypi.python.org/pypi/ironpycompiler/0.9.0
	
	VS:OutputWindow > Log.txt, run app from vs console
    
    
	7.28
	
	Cool ML Researcher, did a ConvNet for Kaggle
	http://ilyakavalerov.com/
	https://news.ycombinator.com/user?id=ilzmastr
	
	
	8.3
	
	Boston FabFest @Roxbury
	http://www.fab11.org/fab-festival/boston-fab-festival/
	
	Python in VS
	http://blogs.msdn.com/b/visualstudio/archive/2015/08/03/why-write-python-in-visual-studio.aspx
	https://news.ycombinator.com/item?id=9998227
	
		useful hint on python compilers
		http://www.decalage.info/en/python/py2exe
	
	Ely Spears in Cambridge MA
	https://careers.stackoverflow.com/ely
	https://news.ycombinator.com/user?id=p4wnc6
	
	8.4
	
	Dr Zoidberg on HN, Python and ML pragmatist
	https://news.ycombinator.com/threads?id=dr_zoidberg
	
	In support of Conda
	http://technicaldiscovery.blogspot.sg/2013/12/why-i-promote-conda.html
	
		Recommended reading - Linkers & Loaders
		http://www.iecc.com/linker/
		
	8.5
	
	DIYbio discussion on Hackaday
	http://hackaday.com/2015/07/30/the-biohacking-movement-and-open-source-insulin/
	
	David from Germany, DIYbio
	https://hackaday.io/dnhkng
	
	ImgProc GUI tool
	http://imageplay.io/
	
	MS has interest in Synbio
	http://research.microsoft.com/en-us/projects/gec/
	
	8.7
	
	Stanord robotics ping pong robot arm http://spectrum.ieee.org/view-from-the-valley/robotics/robotics-software/stanford-students-teach-robots-to-play-pingpong-land-a-drone
	 
	8.10
	Bradley Garrett in Explore Everything: Placehacking the City (2013)
	
	
	8.11
	
	Open Driver implemenetation for Broadcom GPU on Rpi2
	https://wiki.freedesktop.org/dri/VC4/
	
	8.12
	
	IPython -> Jupyter 4.0
	http://blog.jupyter.org/2015/08/12/first-release-of-jupyter/
	
		The big split
		https://blog.jupyter.org/2015/04/15/the-big-split/
		
	Kalman filter - with diagrams
	http://www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/
	
		Kalmna filter Ipython class
		https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python
		
		ODE solvers in Matlab/Python
		http://sys-bio.org/wp-content/uploads/2015/01/introMatlabPythonODEs.pdf
		
			List of SynBio Software
			http://sys-bio.org/downloads/
			
	"Computational Narratives" for IPython 	http://blog.jupyter.org/2015/07/07/project-jupyter-computational-narratives-as-the-engine-of-collaborative-data-science/	
	
	GUIs for SMoothie
	http://www.pronterface.com/
	http://octoprint.org/
		https://github.com/guysoft/OctoPi
			mjpeg streamer 
			http://sourceforge.net/projects/mjpg-streamer/
			https://github.com/jacksonliam/mjpg-streamer
			
	8.17
	
	Science Toolbox
	http://sciencetoolbox.org/
	
	8.21
	
	Livecoding.tv
	https://medium.com/backchannel/the-strange-appeal-of-watching-coders-code-5c677b2c34ec
	
	
	8.24
	Places to get prepared meals:  Blue Apron, Plated, Hello Fresh
	
	Good Tut for Command Line in unix
	https://www.codecademy.com/articles/command-line-commands
	
	8.25
	
	Python / Protein guy - Sebastian Raschka
	http://sebastianraschka.com/Articles/2015_why_python.html
		https://github.com/rasbt
		http://nbviewer.ipython.org/github/rasbt/matplotlib-gallery/blob/master/ipynb/publication.ipynb
		
	Discussion of Coursera
	https://news.ycombinator.com/item?id=10116604
	
	8.26
	
	New face/barcode api for android
	https://news.ycombinator.com/item?id=10120294
	
	
	8.27
	
	D3 in Ipython
	http://www.christianmoscardi.com/blog/2015/08/12/embedding-d3-in-ipython-notebook.html
	
	Nuitka - Python Compiler
	http://nuitka.net/pages/overview.html
	
	8.28
	
	Russian "gave up on YC" entrepreneur - Danil Kozyatnikov
	https://medium.com/@danilka
	
	Edward Perello @DesktopGeneomics - Talk @HackerNewsLondon
	https://vimeo.com/137001197
	
	8.31
	
	Python command line tables
	https://github.com/Leviathan1995/Pylsy
		another one
		https://pypi.python.org/pypi/tabulate
	
	JOVE in NewYorker
	http://www.newyorker.com/tech/elements/how-methods-videos-are-making-science-smarter?intcid=mod
	
	RabbitMQ - messaging service
	http://www.rabbitmq.com/tutorials/tutorial-one-python.html
	
	Python + .NET examples on CodeProject
	http://www.codeproject.com/search.aspx?q=python&x=0&y=0&sbo=kw
	
	9.4
	
	ReScience - Computational Journal
	https://news.ycombinator.com/item?id=10169421
	https://github.com/ReScience/ReScience
		http://sequoia.cs.byu.edu/lab/files/reser2010/proceedings/Gomez%20-%20Replication%20Reproduction.pdf
		
	OpenHour @ PublicLabs, Parts&Crafts 9/9
	http://publiclab.org/openhour
	https://groups.google.com/forum/#!topic/sprout-discuss/_OA4PbkNA3U
	
	FlyPi Fluoro Microscope
	http://2015.igem.org/Team:Cambridge-JIC
	https://twitter.com/jimhaseloff/status/625268933239656448
	
	
  9.10
	
	EdX Hackathon
	http://con.openedx.org/
	
  9.11
	
	AWS in english
	https://www.expeditedssl.com/aws-in-plain-english
	

  9.14						
	http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
	
	https://www.linkedin.com/pulse/cargo-cult-data-science-george-roumeliotis
	
    
	9.15

    asyncio webscraper
    http://aosabook.org/en/500L/a-web-crawler-with-asyncio-coroutines.html
	
	9.17
	
	CytoSolve, 2011
	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3032229/
	http://www.bostonmagazine.com/2012/05/shiva-ayyaduri-email-us-postal-service/
	
	9.24
	
	SQLAlchemy wirteup + HN didscussion
	https://news.ycombinator.com/item?id=10270605
	http://pajhome.org.uk/blog/10_reasons_to_love_sqlalchemy.html
	
	
	Europe during Industrial REvolution - "opposite of crisis"
	http://www.csun.edu/~jaa7021/hist531/Goldstone%20-%20Efflorescences%20and%20Economic%20Growth.pdf#
	
	9.25

	RPi web cam interface
`	https://github.com/silvanmelchior/RPi_Cam_Web_Interface	

	OpenScope Repo, UCamb2015
	https://github.com/sourtin/igem15-sw/
	
	UWash, NitroGenius 2015
	http://2015.igem.org/Team:WashU_StLouis

	10.2
	
	Insight Data Science Bootcamp
	http://insighthealthdata.com/blog/blog1_EmergingField/blog1_emerging_field.html
	
	10.9
	
	IPython + Docker on Rackspace for Nature
	https://developer.rackspace.com/blog/how-did-we-serve-more-than-20000-ipython-notebooks-for-nature/
			
			
	10.14
	Umasser now does programming for bio
	https://news.ycombinator.com/user?id=acomjean
		His lab
		http://perrimon.med.harvard.edu/
	
	R vs Python
	https://news.ycombinator.com/item?id=10386174
	
	10.15
	DIYbio in Nature
	http://www.nature.com/news/biohackers-gear-up-for-genome-editing-1.18236
	
	
	11.2
	Scott Alexander greatest hits
	http://nothingismere.com/2015/09/12/library-of-scott-alexandria/
	
	
	11.4
	
	Smoothie from OpenTrons M114
	https://github.com/Opentrons/SmoothiewareOT
	
	11.5
	ML in Jupyter
	https://github.com/hangtwenty/dive-into-machine-learning
		
		Slide Img: GroundTruth >> Algo's
		https://camo.githubusercontent.com/61e30cc7709455dfa780cc2b0bc4d104b52c7e3c/687474703a2f2f69313338312e70686f746f6275636b65742e636f6d2f616c62756d732f61683234302f68616e677477656e74792f53637265656e25323053686f74253230323031352d30332d3035253230617425323031302e30382e3130253230504d5f7a7073716e6c6a6b7174352e706e67
	
	
		Cool Tricks with Ipython
		http://blog.dominodatalab.com/lesser-known-ways-of-using-notebooks/?hn=2
		
	
	11.6
	
	BioBus
	http://biobus.org/
	
	11.22
	
	OpenInsulin Project
	https://news.ycombinator.com/item?id=10592712
	
	
	11.24
	
	Cheap Kinnect sensor for FlouroLifetime Img
	http://news.mit.edu/2015/biomedical-imaging-lower-cost-1123
		
	Betzig's new lattice light microscope	http://motherboard.vice.com/read/new-microscope-can-see-inside-moving-cells-in-real-time-and-there-are-videos
		
		http://m.sciencemag.org/content/346/6208/1257998.figures-only
		
	Maps of Boston
	http://bostonography.com/
		
		Andy Woodruff
		https://twitter.com/awoodruff
		
		Axis Maps
		https://twitter.com/axismaps
		
		http://maptimeboston.github.io/
		https://twitter.com/maptimeBoston
		
	12.1
	"Welcome, O life! I go to encounter for the millionth time the reality of experience and to forge in the smithy of my soul the uncreated conscience of my race.”
	
	12.8
	
	EMR / Epic rant, link to Phil G
	https://news.ycombinator.com/item?id=10694295
	
	
	The Joint Committee staff recognizes that in lieu of
	including a tax expenditure estimate of the exclusion of investment income on life insurance and
	annuity contracts it may be appropriate to include a tax expenditure estimate of the exclusion
	from gross income of death benefits payable under a life insurance contract by reason of the
	death of the insured. However, an estimate of the tax expenditure of this statutory exclusion is
	not included in the present report. 
	https://www.jct.gov/publications.html?func=startdown&id=4855
	
	
	Google's AI language
	https://www.tensorflow.org/
	
		review
		http://www.technologyreview.com/news/544356/heres-what-developers-are-doing-with-googles-ai-brain/
		
	12.11
	
	OpenSource Cartesian Robot Kit
	http://www.contraptor.org/
	
	12.16
	
	It follows that the Romans were rich not because technological progress temporarily exceeded population growth—as Malthusianists claim—but because Rome had a business-friendly legal system and an active market economy. Well-functioning courts and market-places boost industry more than they boost agriculture. Thus biasing production structure to luxury, they raised the average living standards of the whole society. Conversely, the Agricultural Revolution left an unfortunate legacy: the hunter-and-gatherer-turned peasants failed to achieve the level of leisure and nutrition their ancestors once enjoyed (Diamond, 1987). Growth was immiserizing because agriculture biased production structure to subsistence. The same tragedy recurred when potato dominated the Irish diet in the late 18th century. - See more at: http://marginalrevolution.com/#sthash.8RwZ6Q98.dpuf
	
	12.17
	
	Why Science is a 3rd world Economy
	https://metarabbit.wordpress.com/2013/10/02/why-science-is-a-third-world-economy/
	
	
	12.23
	
	"Folks! Which industries/professions give up their own free time to provide freeopen training to people wishing to enter the sector? Curious" - @koletiv
	Answer:  only one: software development. You want to be a doctor? Go to medical school for seven years
	
	Jupyter notebook extensions
	http://blog.rtwilson.com/an-easy-way-to-install-jupyter-notebook-extensions/
	
	The future of liberalism
	http://www.the-american-interest.com/2012/01/24/the-once-and-future-liberalism/
	
	Seaborn - a python plotting framework
	http://stanford.edu/~mwaskom/software/seaborn/examples/index.html
	
	
	12.28
	
	Moss Viewing Girls (Japan)
	http://ignition.co/398
	
	12.29
	
	Euler Method on MIT Mathlets
	http://mathlets.org/mathlets/eulers-method/#
	
	1.4
	
	It would seem gauche to judge a potential fiance by his wealth or lack thereof. But we would expect him not to be judged on his ethnicity, but whether he had a job, a house etc... things that wealth signifies.
	
	1.6
	
	Filamentous Bacteria conduct electricity!
	http://www.nature.com/nature/journal/v491/n7423/full/nature11586.html
	
	
	1.7
	
	"DOTNET"
	
		CLI  -cmd line interface
		https://github.com/dotnet/cli
	
		Info Page
		http://dotnet.github.io/
	
		API index
		http://dotnet.github.io/api/index.html
	
	
	WCF tut
	http://www.codeproject.com/Articles/406096/A-beginners-tutorial-for-understanding-Windows
	
	Exposition on CIL
	https://en.wikipedia.org/wiki/Common_Intermediate_Language
	
	
	1.11
	
	Kinnect + Arduinos
	http://www.techbitar.com/kinect-controls-servos-using-human-motion.html
	https://channel9.msdn.com/Series/KinectQuickstart/Setting-up-your-Development-Environment
	
	1.13
	
	Caffeine Bacteria	http://blogs.discovermagazine.com/seriouslyscience/2015/12/03/microbiologists-discover-caffeine-adapted-bacteria-living-in-the-sludge-in-their-office-coffee-machine/#.VpZ97vkrJhE
	
	
	Dan Wang, tech blogger
	http://danwang.co/my-2015/
	
	Dotnet Thoery
	
		Notes:
		
		
		CIL - "Common Infrastructure Language" is the language accepted as input in CLR / CLI
		
		CLI - "Common Language Infrastructure" is the actual Infrastructure used to execute the program in CIL, it includes JIT compile to machine code and execution. The CLI is the open standards name for an implementation of the "VM" that will run the program. So Mono and .net are both implementations.
		
		How does the core of the virtualized runtime get distributed with the software? Does it come with a new version of the CLR and GAC it? it doesn't appear to be in the Ascent /bin...Would you need to download a new "JRE"?
		
		JIT for CLR
		http://www.telerik.com/blogs/understanding-net-just-in-time-compilation
		https://msdn.microsoft.com/en-us/library/ht8ecch6(v=vs.90).aspx
		
			Ngen (for VS command line) - native image
			https://msdn.microsoft.com/en-us/library/6t9t5wcf(v=vs.100).aspx
			
			CLR is one of these Virtualization software
			https://en.wikipedia.org/wiki/Comparison_of_application_virtualization_software#cite_note-1
			
			
			https://en.wikipedia.org/wiki/Comparison_of_application_virtualization_software#cite_note-1
			
	
	1.19
	
	
	http://togelius.blogspot.com/2016/01/why-video-games-are-essential-for.html
	
	pacman AI contest (UC Berkley)
	http://ai.berkeley.edu/contest.html
	
	Adrian/OpenCV - how to use threading for Object-Tracking
	http://www.pyimagesearch.com/2015/12/21/increasing-webcam-fps-with-python-and-opencv/
	
	
	webcam:should have support for v4L2
	
	1.20
	
	Robert Gordon - end of American Growth
	http://press.princeton.edu/titles/10544.html
	
		response, Joel Mokyr
		http://www.voxeu.org/article/technological-progress-thing-past
		
		
	1.21
	
	Krugman, comparative advantage
	http://web.mit.edu/krugman/www/ricardo.htm
	
	Why I'm not an objectivist
	http://www.owl232.net/rand.htm
	
	
	1.22
	
	Google DeepLearning course on udacity
	https://www.udacity.com/course/deep-learning--ud730
		
		discussion on HN
		https://news.ycombinator.com/item?id=10951276
		
			recommended other course
			http://neuralnetworksanddeeplearning.com/chap2.html
		
		
	“Each man takes care that his neighbor shall not cheat him. But a day comes when he begins to care that he does not cheat his neighbor. Then all goes well - he has changed his market-cart into a chariot of the sun.”  -Emerson
	
	1.25
	
	Robot Sailboat
	http://blog.kragniz.eu/
	
	Blog of ArtDeco, the commenter on MR
	http://wwrtc.blogspot.com/
	
	junk, or?
	https://databricks.com/
	
	MS neural nets on Azure	http://blogs.microsoft.com/next/2016/01/25/microsoft-releases-cntk-its-open-source-deep-learning-toolkit-on-github/
	
	
	Bio-Talk
	https://news.ycombinator.com/item?id=10964118
	
	
	1.26
	
	Deep Learning Frameworks on GSheet	https://docs.google.com/spreadsheets/d/1XvGfi3TxWm7kuQ0DUqYrO6cxva196UJDxKTxccFqb9U/edit#gid=0
	
	MediaLab Synbio for the Masses essay	https://medium.com/mit-media-lab/synbio-for-the-masses-a-media-lab-grad-s-deploy-or-die-story-dc712311079a#.z2rpcjtq2
	
	1.27
	
	Patchable VideoGame
	http://www.illucia.com/
	
	Molecular Machinery
	http://mm.rcsb.org/
	
	
	CRSIPR spreadsheet from Addgene	http://blog.addgene.org/the-crispr-software-matchmaker-a-new-tool-for-choosing-the-best-crispr-software-for-your-needs?utm_campaign=CRISPR-Cas9&utm_content=28333312&utm_medium=social&utm_source=twitter	
		https://docs.google.com/spreadsheets/d/1ik3GWCoRVS74x7lDt2tPjWg9pVFEtaTPCd-LEzBoMUE/edit#gid=1285541112
	
	
	reconstructing-position-from-depth	https://mynameismjp.wordpress.com/2009/03/10/reconstructing-position-from-depth/
	
	
	http://dotnet.github.io/api/System.Array.html
	https://msdn.microsoft.com/en-us/library/yw84x8be(v=vs.110).aspx?cs-save-lang=1&cs-lang=vb#code-snippet-1
	
	
	1.28
	
	Human/Robot UX	http://humanrobotinteraction.org/2015/program-2/proceedings-table-of-contents/

		Direction for flyers	http://delivery.acm.org/10.1145/2700000/2696475/p19-szafir.pdf?ip=71.174.214.162&id=2696475&acc=OPENTOC&key=4D4702B0C3E38B35%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35%2E9F04A3A78F7D3B8D&CFID=748498233&CFTOKEN=97784456&__acm__=1454002657_8fada89da483de7d76c6754b8215ea0d
	
	
	Keith Hennessy, CBO
	http://keithhennessey.com/
	
	Argonaut project for FHIR, EHR interop
	http://hl7.org/fhir/2015Jan/argonauts.html
	
	
		Interop advocate for EHR's	http://www.forbes.com/sites/davidshaywitz/2016/01/18/the-last-best-chance-to-achieve-interoperability/2/#1c0cda164509
		
		https://open.epic.com/AppExchange/Sandbox
	
		Fire, Fire on the mountain
		https://fhir.catalyze.io/
	
	
	Ping Pong Drone!
	http://mentalfloss.com/article/71607/ibm-researchers-built-drone-can-play-ping-pong
	
		YT url
		https://youtu.be/YvbHXz3lccc
		
		them boys
		http://researcher.watson.ibm.com/researcher/view_group.php?id=1403
	
		RPi drone
		https://youtu.be/LWwkB6hGD4M
		
		Engineering team blog, Pool openCV, 2012
		https://gocardless.com/blog/hacking-on-side-projects-the-pool-ball-tracker/
	
	
	BioDesign Challenge
	http://biodesignchallenge.org/
	
	
	Adrian, OpenCV dude
	
		imutils, for use with opencv
		https://github.com/jrosebr1/imutils
			https://pypi.python.org/pypi/imutils/0.3.4
			
		supported webcams for Rpi
		http://elinux.org/RPi_USB_Webcams
		
		Increase FPS with Threading, on PC-USBWebcam
		http://www.pyimagesearch.com/2015/12/21/increasing-webcam-fps-with-python-and-opencv/
		
	Logitech c920
	
		- Full HD 1080p video calling (up to 1920 x 1080 pixels) with the latest version of Skype for Windows
		- 720p HD video calling (up to 1280 x 720 pixels) with supported clients
		- Full HD video recording (up to 1920 x 1080 pixels) 
		- H.264 video compression
		- Built-in dual stereo mics with automatic noise reduction
		- Automatic low-light correction
		- Tripod-ready universal clip fits laptops, LCD or monitors
	
	
		software
		http://support.logitech.com/en_us/product/hd-pro-webcam-c920
		
		docs
		http://www.logitech.com/assets/45920/hd-pro-webcam-c920-quick-start-guide.pdf
		
		Others have slow frame rate, do 4:3 ratio, as metro ratio is killing it
		http://answers.microsoft.com/en-us/windows/forum/windows8_1-winapps/in-windows-81-the-camera-app-sometimes-lags-or-is/aa16f265-c38f-40aa-ba2f-21f26dfc9941?db=5&auth=1
	
	
			Kinovea, Sports CV - by Joan Charmant
			http://www.kinovea.org/
			
				blog -> measuring angles in perspective
				
				http://stackoverflow.com/users/867395/joan-charmant

	2.3 

		CV2 / Camera research
		
			FPS, other issues
			http://forums.logitech.com/t5/Webcams/H264-c920-api/td-p/861862
			
			
			USB branches
			http://www.uwe-sieber.de/usbtreeview_e.html
			
			
			DirectShow, .net api for video streams and video devices
			https://msdn.microsoft.com/en-us/library/windows/desktop/dd375454(v=vs.85).aspx
			
			Logitech c920 support forum:
			I think you need to switch to a different capture pin. I believe there are three. The first for video which you seem to have used. The second for still capture and the third which captures video in H264 only. I have used this capture pin with graphedit and connected it to the ffdshow filter and can confirm it works.
			
			no 60fps :(
			https://obsproject.com/forum/threads/logitech-c920-60fps.8407/#post-73983
			
			no 60fps? - but still, turn off "right light"
			https://www.reddit.com/r/Twitch/comments/2r3jjh/c920_60_fps/
			
			Application needs to handle H264 cenoded stream for max-thruput http://stackoverflow.com/questions/13113560/processing-c920-logitech-capture-frame-rate-video-discourse
			
			How to set camera from CV2	http://stackoverflow.com/questions/16092802/capturing-1080p-at-30fps-from-logitech-c920-with-opencv-2-4-3?rq=1
		
				OpenCVs APIs	http://stackoverflow.com/questions/14187866/opencv-on-mac-is-not-opening-usb-web-camera/14188280#14188280
		
	2.4
	
		Idea DEBT!
		http://jessicaabel.com/2016/01/27/idea-debt/
		
		"The new wave of science communicators"
		http://crastina.se/
		
		Lucy two laptops gif
		http://pandawhale.com/post/58011/scarlett-johansson-hacking-on-two-laptops-gif
		
		Synechocystis as eyeball	http://www.theatlantic.com/science/archive/2016/02/this-bacterium-acts-like-a-one-cell-eyeball/460500/
		
		
	2.10
		
		Chip MicroDrone $14	http://www.gearbest.com/rc-quadcopters/pp_230472.html?utm_source=Criteo&utm_medium=CPCUS&utm_campaign=Displayads&vip=87199
		
		RoboMicro for Malaria
		https://www.technologyreview.com/s/600779/artificial-intelligence-offers-a-better-way-to-diagnose-malaria/
		
		
	2.12
	
		Microsoft Dance Party
		https://www.facebook.com/thenextweb/videos/10153895531388523/
		
		
	2.16
	
		Teacher?https://educationrealist.wordpress.com/2016/01/31/note-from-a-trump-supporter-its-the-immigration-stupid/
		
		Beyond MVC, new patterns
		http://www.infoq.com/articles/no-more-mvc-frameworks
		
		Drone flight simulator! (but linux only (?) :/ )
		https://github.com/motet/baldr
		
			could use blender for 3d rendering
			https://www.blender.org/about/
			
			or use "morse"
			https://www.openrobots.org/wiki/morse/
			
		Dark was the night, Cold was the Ground
		https://www.youtube.com/watch?v=qePHCNoEtqQ
		
	2.17
	
		“The impediment to action advances
		action. What stands in the way becomes
		the way.” ― Marcus Aurelius

	2.18
	
		Tax Visuzaliztion, only remnant still available (?)
		http://www.datavizchallenge.org/viz/71
		
			statically here too
			http://www.two-n.com/projects/taxmapper
			
			it works on wayback machine
			https://web.archive.org/web/20110415083303/http://stockmapper.com/taxMapper.html
			
		
		Engineer @Formlabs, MechE who did cool project to get job
		http://shane.engineer/
		
		9600 bps and 115200 bps
		
	2.22
	
		Matt's Kickstarter for tuition
		https://www.generosity.com/education-fundraising/hive-or-bust-matthew-s-tuition
		
		
	2.24
	
		Math & Programming
		http://jeremykun.com/
		
	2.25
		
		Driving Bot
		http://matpalm.com/blog/drivebot/
		
			other interesting stuff- using theano with GPUs
			http://matpalm.com/blog/2015/02/22/the_curse_of_gpufromhost/
		
		Jupyter Days	https://www.eventbrite.com/e/jupyterdays-boston-2016-tickets-21440120979?cmp=mp-mh-na-na-reg-ug-11855_343_pc
		
		C# on edX
		https://www.edx.org/course/programming-c-microsoft-dev204x-1
		
	3.2
	
		Jeff Pincus
		https://www.linkedin.com/in/jeffry-pincus-518b393a
		
	3.3
		“I have observed that not the man who hopes when others despair, but the man who despairs when others hope, is admired by a large class of persons as a sage.”
		-JS Mill wrt K Marx (from B Gates)
		
		
	3.4
	
		Robots and Vision Textbook online
		http://www.petercorke.com/RVC/top/toc/toc.pdf
		
		Robo-simulator
		http://www.robotvirtualworlds.com/
		
		PLOS talks DIYbio hardware http://blogs.plos.org/synbio/2016/03/01/open-source-hardware-is-an-opportunity-for-synthetic-biology-research-the-docubricks-approach-by-tobias-wenzel/
		
		
		
	3.18
		
		GPU for life insurance. Yay!
		also RungeKutta ODE's
		https://devblogs.nvidia.com/parallelforall/gpus-dsls-life-insurance-modeling/
		
			GPU's for .net
			https://devblogs.nvidia.com/parallelforall/accelerate-net-applications-alea-gpu/
		
		Travis Pittman, Epic Integration for Genospace "HL7 messages"
		https://www.linkedin.com/in/travis-pittman-88b1a620?trk=pub-pbmap
		
		
	3.21
	
		The revolutionary mentality, an enemy to the human spirit
		http://www.olavodecarvalho.org/english/articles/070813dc_en.html
		
	3.23
	
		"Voters are better at signaling dissatisfaction than thinking clearly about solutions."
		- Holman Jenkins
		
	3.24

		YC W2016
		https://startups.watch/yc-w16-startups/

	3.29
	
		Audre Lorded, on the Erotic's connection to everyday modern life
		http://www.metahistory.org/guidelines/EroticUses.php
		
			"Our erotic knowledge empowers us, becomes a lens through which we scrutinize all aspects of our existence, forcing us to evaluate those aspects honestly in terms of their relative meaning within our lives."

	3.30
	
		Feather, R & Python Dataframes in external storage
		http://blog.rstudio.org/2016/03/29/feather/
		
			https://github.com/wesm/feather
			
			built by Wes McKinney, interesting BI/dev guy
			http://wesmckinney.com/
			https://github.com/wesm
			
	
	3.31
	
		DNA Lecture
		https://www.statnews.com/2016/03/31/dna-shape-double-helix-dekker/
	
		VisualStudio + Xamarin for Free
		https://news.ycombinator.com/item?id=11398033
		
		CivII game mired in stalemate
		http://kernelmag.dailydot.com/issue-sections/headline-story/16223/james-moore-eternal-war-a-decade-of-civilization/
			
			
	4.1
	
		Natvis: customize your windows in VS, promising!
		https://msdn.microsoft.com/en-us/library/jj620914(v=vs.110).aspx#BKMK_ArrayItems_expansion
			
			
			https://msdn.microsoft.com/en-us/library/system.diagnostics.debuggerdisplayattribute.aspx
			
			
			http://stackoverflow.com/questions/8348869/visualstudio-debug-array-tooltip-class-value
			
			http://stackoverflow.com/questions/369192/is-there-a-way-to-customize-the-tool-tip-of-a-custom-object-in-the-vs-debugger
			
			http://stackoverflow.com/questions/23993284/is-there-a-way-to-tell-visual-studio-to-show-certain-member-values-by-default-wh?rq=1
			
			Fix DataTips for parameterized property access... #3897
			https://github.com/dotnet/roslyn/pull/3897
			
			
			https://github.com/dotnet/roslyn/issues/2602
			
			<DebuggerDisplay("HOVA")>
			 Public Class .....
			 
				<DebuggerBrowsable(DebuggerBrowsableState.Collapsed)> _
				public arr() as integer
		
		Google Sheets ODBC for VisualStudio
		http://www.cdata.com/drivers/gsheets/odbc/
			
	4.4
	
		Mac, back at it
		https://news.ycombinator.com/threads?id=100ideas
			
		Cello!
			writeup: http://phys.org/news/2016-03-language-cells.html
			paper: http://science.sciencemag.org/content/352/6281/aac7341
			site: http://www.cellocad.org/index.html
			discussion: https://news.ycombinator.com/item?id=11417689
			repo: https://github.com/CIDARLAB/cello
			nielsen2016: https://sci-hub.io/download/c7c5/nielsen2016.pdf
			cidar @bu: http://cidarlab.org/cello/
			
			
		The Xamarin thing, here
		https://www.xamarin.com/download
		
	4.5
	
		Lily Cua, benefits entrepreneur
		http://aspire.is/
		http://www.nytimes.com/2016/04/10/education/edlife/will-you-sprint-stroll-or-stumble-into-a-career.html
		
	4.6
	
		“Donna and most nurses are very open-minded,” he said. “They’ve seen it all—death, disease, pain, disorders of every kind—and it takes a lot to shock a nurse.” -G Talese
			
		“Man cannot see too much of human nature.” 
		
	4.11
	
		Trevor Murphy, independant student actuary, did Data Science bootcamp
		https://www.linkedin.com/in/trevor-murphy-49ba1421
			http://signaldatascience.com/projects/
			
		
	4.12
	
		The Life of Cell Watchers
		http://www.amazon.com/Lives-Cell-Notes-Biology-Watcher/dp/0140047433
		
	4.13
	
		Didn't blank out the black guy's face  https://www.google.com/maps/@42.3554941,-71.055546,3a,35.1y,339.94h,78.11t/data=!3m6!1e1!3m4!1szqrwu_pz_YyTC7zz6he2Jg!2e0!7i13312!8i6656
		
		
		Cambridge Science Festival:
		http://www.cambridgesciencefestival.org/2016Festival/EventIndex.aspx
		
		4/20  (also Saturday 4/23, same time)
		1:00pm - 4:00pm
		Sailing Science: Robotic Sailing & Environmental Science at Community Boating, Inc.
		Community Boating Boathouse, 21 David G Mugar Way, Boston
		
		4/21	
		6:30pm - 8:00pm
		Science Pint Night
		Rattlesnake Bar and Grill, 384 Boylston St, Boston
		Come enjoy a pint while hearing from our scientist panel representing various labs from MGH and Tufts University, who will be showcasing their own cutting-edge work!  It will be an evening of 4-minute info-packed talks about current hot topics at the forefront of different scientific fields.  Make sure you stick around after the session for an opportunity to mingle! 
			
	4.14
	
		Xamarin + Emgu -> Android OpenCV !!
		http://file.emgu.com/forum/viewtopic.php?t=8132
			
			 but you need licenses? http://www.emgu.com/wiki/index.php/Commercial_License_Purchase#Commercial_License_3.0_for_Windows
			
			HowTo for Android
			http://www.emgu.com/wiki/index.php/Emgu_CV_for_Android
			
				my question on forum
				http://www.emgu.com/forum/viewtopic.php?f=7&t=7999&p=16520#p16520
				
			
			Regan's app http://file.emgu.com/wiki/files/3.0.0-rc1/document/html/7683e464-4f6e-4221-573f-b3338ded37ad.htm
			http://www.masslottery.com/games/lottery/winning-keno-numbers.html
			
	4.19
	
		How guy got into electronics Hacking - How a diode changed my life
		http://onurcelebi.com/blog/how-a-diode-changed-my-life/
			
		
		Get actualized quick scheme
		http://www.onescientist.com/
		
	4.24
	
		Rex St. John on Makers, son of the saint
		http://rexstjohn.com/meet-the-inventors-the-accelerators-of-the-maker-movement/
		
		
		Survivalist stuff
			http://www.rapidtrends.com/surving-argentinas-economic-collapse-part-1-3/
			http://www.amazon.com/Modern-Survival-Manual-Surviving-Economic/dp/9870563457/
			
		SouthShoreScience, in Quincy
		http://southshorescience.org/
			
	4.25
		
		DroneSmith, motherfucker. An Intel platform/hardware as a service company
		http://www.dronesmith.io/about/
		
			slack channel
			http://community.dronesmith.io/
			https://dronesmith-community.slack.com/messages/general/
				
			Read the docs!
			https://dronesmith.readme.io/docs
			
			A Python API to the Flightcore?
			http://python.dronekit.io/about/overview.html

			Formerly Skyworks Aerial Systems, $1M funding, based in vegas
				https://www.crunchbase.com/organization/skyworks-aerial-systems#/entity
				
				https://angel.co/dronesmithtech
			
			
		Discussion on edX
		https://news.ycombinator.com/item?id=11562468
			
			
	4.26
	
		Dylan breaks it down
		https://www.youtube.com/watch?v=SfPSCDu6NQ4
		
			upbeat and jamming
			https://www.youtube.com/watch?v=uVFy2YEkoLo
			
		"The physics of software is not algorithms, data structures, languages and abstractions. These are just tools we make, use, throw away. The real physics of software is the physics of people—specifically, our limitations when it comes to complexity, and our desire to work together to solve large problems in pieces. This is the science of programming: make building blocks that people can understand and use easily, and people will work together to solve the very largest problems."
			-http://zguide.zeromq.org/py:all
			
		
		Perfect for Logging in Python
		http://zguide.zeromq.org/py:all	
			
		Dying dude of ZMQ
		https://www.youtube.com/watch?v=O8CbzKREAj4
			
			
	4.27
	
		Throwing rocks at the Google Bus
		http://www.amazon.com/Throwing-Rocks-Google-Bus-Prosperity/dp/1617230170
		
		Xamarain Andorid Repo
		https://github.com/xamarin/xamarin-android
			
	4.28
	
		OpenAI Gym
		https://gym.openai.com/
		
			Discussion on HN
			https://news.ycombinator.com/item?id=11582345
		
			Wrtie-up on OpenAI Gym for robot reinforcement learning	https://www.technologyreview.com/s/601349/good-robot-elon-musks-ai-nonprofit-shows-where-ai-is-going/
			
			
			Reinforcement learning write-up			https://www.technologyreview.com/s/544521/a-master-algorithm-lets-robots-teach-themselves-to-perform-complex-tasks/
		
			
		Kaggles Repo of Jupyter Notebooks
		https://www.kaggle.com/scripts?sortBy=votes&language=Python&outputType=Notebook
			
			Ben Hamner, now CTO
			https://news.ycombinator.com/user?id=benhamner
			
		Udacity course on Algos
		https://www.udacity.com/course/viewer#!/c-cs215/l-48723544/m-48723447
		
		
		Controlling mini drone with an arduino	https://www.hackster.io/geekphysical/controlling-toy-quadcopter-s-with-arduino-6b4dcf?ref=list&ref_id=3056&offset=16
			
			Controlling Mini-drone form the internets
			https://www.hackster.io/virgilvox/iot-drone-swarm-22f36a
		
			"parrot rolling spider drone"
			https://github.com/octoblu/meshblu-rolling-spider#readme
			https://www.hackster.io/parrot/products/travis-airborne-cargo-drone
			
			And with hand gestures	https://www.hackster.io/andrewstein/control-your-drone-swarm-with-hand-gestures-2fd3cd?ref=similar&ref_id=15927&offset=4
			
		
		Kickstarter for co-drone, the learn to code, and programmable drone
		https://www.kickstarter.com/projects/728836843/codrone-learn-to-code-with-programmable-drone
		
			
		Hod Lipson, Roboticist, Dennis' Boss
		http://www.hodlipson.com/
		
		http://www.ted.com/speakers/hod_lipson
		
			Model(step = s) -> "Most-controversial" Predictions  -> Execute and Evaluate -> ...
		
			Roboevents for kids
			http://www.robotevents.com/index.php
			
			
			
	5.1
	
		Airware (drone) blog
		https://makers.airware.com/
		
	5.3
	
		Drink Botulism Thought experiment: 
		Say your eating something and a scientist is like "Hey, there's probably Botulism in that"
		You could be like "Doubt it, we'll see though and if I start getting the symptoms, I'll stop eating it."
		Symptoms occur 18-36 hours. You'll be done eating the food in 15 minutes.
			
			
	5.6
	
		AI Kaggle
		http://theaigames.com/
		
		Jobs at OpenAI
		https://jobs.lever.co/openai
		
		
		XKCD matplotlib style
		http://jakevdp.github.io/blog/2013/07/10/XKCD-plots-in-matplotlib/
		
			Video in IPython
			from IPython.display import HTML
			url = 'http://jakevdp.github.io/downloads/videos/double_pendulum_xkcd.mp4'
			HTML('<video controls alt="animation" src="{0}">'.format(url))
			
		
		Machine Intelligence Landscape, Shivon Zilis (partner at OpenAI)
		https://www.oreilly.com/ideas/the-current-state-of-machine-intelligence-2-0
		
	5.10
	
		Chinese Scholar, 1999: Unrestricted Warfare
		http://www.cryptome.org/cuw.htm
			
	5.12
	
		 "While I think that many of the architectural criticisms are valid, Rails demonstrates the primacy of ecosystem and strong conventions over language design and cs theory." 
		  
	     "think people overestimate the importance of understanding a line in isolation and underestimate the importance of understanding a whole component or system. A one-screen class where you have to spend a couple of seconds understanding each line feels harder to read than a three-screen class where each line is simple, but (IME) ends up being more maintainable."
		 
		 "Rails's original popularity came from developers fleeing the excessive ceremony and boilerplate code of enterprise Java – and .NET to some extent."
		 
		 -HN comments
		 
		Philosophy startup? 
		 https://www.mailpoet.com/author/keiferszurszewski-after-plato/
		 
		
		Here's how I did it.
		I emailed any technical contact I could find at all the interesting companies in my city. I was following up all these emails with phone calls when I could get a number.
		I found a blog article interviewing one of the researchers (call him Bob) at "Company A".
		I sent this email that eventually led to my job:
		Hello Bob, I've been researching [Company A] and came across this article from [BLOG SITE] that featured some of your work. I'm quite impressed with your assessment of the need for better data analysis tools in the [AREA OF RESEARCH], and the work you get to do in that area interests me. I found from your linkedin profile that part of your current research with the Company A Research Group is on [technical area I talk about below].
		My recent PhD work at [University] involved a number of overlaps with your current work, both in technology ([short example]) and modeling physical processes ([short example]).
		I am now looking for industry jobs in [City]. The Company A Research Group may be a good fit, but first I would like to learn more about what you do. Can you meet for coffee to discuss?
		Best regards, -[my name]
		He responded and asked for a resume. After further conversations, it turned out they didn't have room in their group (headcount freeze in their department) but we found another group at the company that needed someone with my skills. I was then "the guy Bob knows" during the interviews (which helped) and landed the job.
			
		
	5.13
	
		Drone for $130
		http://uav-rc.com/products/zmr-250-arf-quadcopter-cc3d-kit
		
		
	5.16
	
		HN who's a actuary -> software dev
		https://news.ycombinator.com/user?id=thedevil
		
		Letters from A Young Biologist, CoryTobin DIYbio nitrogen fixing (via Mac)
		https://medium.com/@davidtlang/letters-from-a-young-biologist-f0374851dbc4#.mmnkg4gd8
		
		David Lang, From Zero to Maker, openROV guy, citizen sci enthusiast
		https://medium.com/openexplorer-journal
			
			https://medium.com/ted-fellows/how-my-10-000th-day-in-the-world-changed-my-life-b9fd976a1373#.5anfeermi
			
	5.17
	
		Websupergoo help page
		http://www.websupergoo.com/helppdfnet/source/3-concepts/b-htmlstyles.htm?q=stylerun
	
		PingPong Robot - "TrainerBot" - Pitching machine
		Alex & Harrison @HAX
		
			http://www.trainerbot.com/
		
			https://www.kickstarter.com/projects/1743882979/trainerbot-smart-ping-pong-robot
			
			https://www.facebook.com/trainerbot/?fref=photo
		
			http://www.theverge.com/circuitbreaker/2016/5/17/11690268/trainerbot-robot-ping-pong-hands-on
		
		
		Deep Mind writeup, 2015
		http://www.wired.com/2015/12/teaching-ai-to-play-atari-will-help-robots-make-sense-of-our-world/
		
			Skymind, Adam Gibson '14
			http://www.wired.com/2014/06/skymind-deep-learning/
			
		Zipfianacademy, become a data scientist, now Galvanize
			deprecated: http://www.zipfianacademy.com/
			
			http://www.galvanize.com/courses/
			
		
	5.18
		
		Richard Sutton, Reinforcement Learning 1998
		http://webdocs.cs.ualberta.ca/~sutton/book/ebook/node7.html
		
		
		CS 188 UC Berkley
			
			Reinforcment II
			https://www.youtube.com/watch?v=yNeSFbE1jdY
			
		Python Cartpole by Jeremy Stober @DepthFirstSearch.net
		https://github.com/stober/cartpole/blob/master/src/__init__.py
		
		Cartpole solved by pyBrain.RungeKujtta method
		http://pydoc.net/Python/PyBrain/0.2.1/pybrain.rl.environments.cartpole.cartpole/
			http://pybrain.org/
			
			
		Nick Lane on Gates Notes
		https://www.gatesnotes.com/Books/The-Vital-Question
			
			
	5.23
	
		Ipython notebook for criminal sentencing, probulica expose
		https://github.com/propublica/compas-analysis/blob/master/Compas%20Analysis.ipynb
		
	5.24
	
		Former MS Exec, fucked over .net devs
		https://blog.learningbyshipping.com/
		
			https://twitter.com/stevesi
		
			article calling him out
			https://news.ycombinator.com/item?id=11761437
			
	5.27
	
		Voight video
		https://www.youtube.com/watch?v=lNttxYdGHs4&feature=youtu.be
			
		Aegis! - Defend yourself against microsoft
		https://github.com/th3power/aegis-voat
		
	6.1
	
		AI stuck at local min: http://kennethfriedman.org/projects/escaping-local-min/
	
		Karpathy, RL writeup
		http://karpathy.github.io/2016/05/31/rl/
			
			karpathy github https://github.com/karpathy
			@stanford: http://cs.stanford.edu/people/karpathy/
		
	
		Learn Docker by building a sample node app
		http://www.dwmkerr.com/learn-docker-by-building-a-microservice/
		
		CodePlex - MS's github, mostly C# stuff
		https://www.codeplex.com/
		
		Visual Studio Extension tutoriala
		http://www.codeproject.com/Articles/324611/Extending-Visual-Studio-Part-Creating-Addins
		
		Dan Luria, director of engineering @societyofgrownups
		http://www.meetup.com/Boston-Young-Creatives/members/9250589/
		https://news.ycombinator.com/threads?id=whichdan
		
		Chaitin incompletness theory sketch
		http://math.ucr.edu/home/baez/surprises.html
		
		Demo of NN http://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.18822&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false
		
		
	6.10
	
		Async RL + OpenAI gym
		https://github.com/coreylynch/async-rl
		
		Paxos consensus algo
		https://en.wikipedia.org/wiki/Paxos_(computer_science)
		
		
	6.13
	
		Cambridge Coding - recommender systems in python	http://online.cambridgecoding.com/notebooks/eWReNYcAfB/implementing-your-own-recommender-systems-in-python-2
		
		Queue in C++ for event driven programs
		http://ithare.com/implementing-queues-for-event-driven-programs/
		
		Curated Recommender for Films
		https://www.film-fish.com/
		
		
		