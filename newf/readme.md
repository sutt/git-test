
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
		
		Zuck bro http://thenextweb.com/facebook/2016/04/18/check-old-zuckerberg-interview-facebook-solo-cups-keg-stands/
		
		Now to the Neolithic - lecture by history of sci teacher
		http://derekdesollaprice.org/
		
		HN user, Jason Huggins, does robot that plays angry birds
		https://news.ycombinator.com/user?id=hugs
		http://www.tapster.io/
		
		Example Tindie item
		https://www.tindie.com/products/2bluesc/cleanhawk-250-quadcopter-power-distribution-board/
		
	6.15
	
		Dirge without Music, Edna St Vincent Millay
		http://www.poetryfoundation.org/poems-and-poets/poems/detail/52773
		
			I am not resigned to the shutting away of loving hearts in the hard ground.
			
	6.21
	
		FTL primer
		http://math.ucr.edu/home/baez/physics/Relativity/SpeedOfLight/FTL.html
		
		IOT list of good software and hardware
		https://github.com/HQarroum/awesome-iot
			
		Trojan Records YT channel
		https://www.youtube.com/channel/UCSREcFC7aALeaDd9Z7zWffw
			
		Gun control proposal from Ars Technica founder
		https://github.com/jonstokes/shootercontrol
		
		10 rules of robot ops
		http://robotops.com/
		
		.net arduino dev for robot
		https://www.youtube.com/watch?v=-Jsvg6u9CYI
		
	6.23
	
		CodeDOM in .net ~ useful?
		https://msdn.microsoft.com/en-us/library/system.codedom(v=vs.110).aspx
			proly not, it only creates code, doesn't interpret it
			
		Xamarin notebooks
		https://developer.xamarin.com/guides/cross-platform/workbooks/
		
		Opening up Makers to robots, via Intel Edison
		http://motherboard.vice.com/blog/opening-up-the-world-of-robotics
	
			talking about: http://hybridgroup.com/
			
		Roslyn walk-thru
		https://roslyn.codeplex.com/wikipage?title=Samples%20and%20Walkthroughs&referringTitle=Home
		
		Q-learning in openAI
		http://nbviewer.jupyter.org/github/patrickmineault/xcorr-notebooks/blob/master/Q-Learning%20&%20OpenAI%20gym.ipynb?utm_content=buffer2e35d&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer
		
		
		Vision guy at google
		https://github.com/patrickmineault
		
		
		How to show openAI games in Ipython notebook
		http://nbviewer.jupyter.org/github/patrickmineault/xcorr-notebooks/blob/master/Render%20OpenAI%20gym%20as%20GIF.ipynb
		
	6.30
	
		"I imagine a project where individual voters go out and find a friend who plans to vote for the other candidate. And then have “the friendly chat that the media is trying to stop us from having”. Not a debate, not another grassroots campaign, just a chat across bubbles. What does my candidate look like to you? Here are three things I like about your candidate. What do you like about your candidate? Can you name three things you like about mine? What parts of the picture do you think I’m missing?"
			-Daniel Bottger http://www.scottaaronson.com/blog/?p=2777
		
		
	7.6
	
		Literate Testing
		https://web.archive.org/web/20110227092515/http://www.arrenbrecht.ch/testing/index.htm
		
			doctest
			https://docs.python.org/2.7/library/doctest.html
		
		
	7.7
	
		Literate Programming write-up	http://www.johndcook.com/blog/2016/07/06/literate-programming-presenting-code-in-human-order/#.V32uxZvDTmQ.hackernews
		
			book by Knuth	https://www.amazon.com/Literate-Programming-Center-Language-Information/dp/0937073806/ref=as_li_ss_tl?ie=UTF8&qid=1467815523&sr=8-1&keywords=literate+programming&linkCode=sl1&tag=theende-20&linkId=8ac40296b143696473fcb8472cab99e3
		
		
	7.12
	
		New Visualizations for Molecular Biology
		http://www.nature.com/news/the-visualizations-transforming-biology-1.20201
		
		
		Optogenetics Open Hardware
		http://web.stanford.edu/group/dlab/optogenetics/hardware.html
		
		
		Caution for DIY brain stimulations tDCS
		https://news.ycombinator.com/item?id=12078895
		
	7.15
	
		Jupyter, next step
		https://news.ycombinator.com/item?id=12098180
		
	7.19
	
		DataTips Galore

		
		
		Motivating StackOverflow complaint				http://stackoverflow.com/questions/30113725/missing-intellisence-data-tip-for-a-datarow-item-in-vs-2012-and-beyond
			https://github.com/dotnet/roslyn/issues/2602
		
		The docs on this
		https://msdn.microsoft.com/en-us/library/ea46xwzd(v=vs.140).aspx
		
		https://msdn.microsoft.com/en-us/library/zayyhzts.aspx
		
		DebuggerDisplay
		https://msdn.microsoft.com/en-us/library/x810d419.aspx
		
		Custom views of Managed Objects
		https://msdn.microsoft.com/en-us/library/zf0e8s14.aspx
		
		Enhanced Views
		https://msdn.microsoft.com/en-us/library/ms228992.aspx
		
		RootHidden
		https://msdn.microsoft.com/en-us/library/system.diagnostics.debuggerbrowsablestate.aspx
		
		AttributeDisplay
		https://msdn.microsoft.com/en-us/library/system.diagnostics.debuggerdisplayattribute.aspx
		
		
		<DebuggerDisplay("HOVA")>
			 Public Class .....
			 
				<DebuggerBrowsable(DebuggerBrowsableState.Collapsed)> _
				public arr() as integer
				
				
	7.20
	
		Windows 10 Developer Mode
		http://www.hanselman.com/blog/Windows10DeveloperMode.aspx
		
		
		How to write a VS visualizer
		https://msdn.microsoft.com/en-us/library/e2zc529c.aspx
		
			OpenTabs
			https://msdn.microsoft.com/en-us/library/ea46xwzd.aspx
			https://msdn.microsoft.com/en-us/library/zayyhzts.aspx
			https://msdn.microsoft.com/en-us/library/e2zc529c.aspx
			https://msdn.microsoft.com/en-us/library/ms164759.aspx
			https://msdn.microsoft.com/en-us/library/microsoft.visualstudio.debuggervisualizers.idialogvisualizerservice.aspx
			https://blogs.msdn.microsoft.com/visualstudio/2016/03/30/visual-studio-2015-update-2-rtm/
			https://blogs.msdn.microsoft.com/visualstudio/2016/02/10/visual-studio-2015-update-2-ctp/
			https://www.visualstudio.com/news/vs2015-update2-vs
			
	7.25
	
		Americas Greatest Makers casting call
		http://venertainment.com/America-s-Greatest-Makers/
		
		In the beginning, there was the command line
		http://cristal.inria.fr/~weis/info/commandline.html
		
		Ask Polly: do what you love
		http://nymag.com/thecut/2014/09/ask-polly-i-hate-my-job-what-should-i-do.html
		
	7.27
	
		Quantopian PR
		http://www.wsj.com/articles/steven-a-cohens-newest-bet-do-it-yourself-computer-traders-1469592001
		
		AXA_Bug
		
		Find IIS on Windows Server
		https://technet.microsoft.com/en-us/library/jj635847(v=ws.11).aspx
		
		Tutorial - deploy asp.net to azure via VS2015
		https://azure.microsoft.com/en-us/documentation/articles/web-sites-dotnet-get-started/
		
		Doesn't work on Azure?
		https://sourceforge.net/p/btnet/discussion/226938/thread/9d18e189/
		
		Installation guide
		http://ifdefined.com/README.html#installation
		
	7.28
		
		http://www.avclub.com/article/best-films-2016-so-far-v-clubs-catch-guide-239983
	
		Scott Tobias - Kiss Kiss Bang Bang
		http://www.avclub.com/article/the-new-cult-canon-ikiss-kiss-bang-bangi-2300
		
	7.29
	
		Blogosphere is best for studying subjects
		http://www.ft.com/cms/s/0/e460ba78-5379-11e6-9664-e0bdc13c3bef.html#axzz4FoZQQcXq
		
	8.1
	
		Numpy whitepapaer
		https://hal.inria.fr/inria-00564007/document
		
		Neumitra - origins story
		http://ilp.mit.edu/newsstory.jsp?id=21222
		
		Abe Connelly on HN
		https://news.ycombinator.com/threads?id=abetusk
		c
			His Repo of learning
			https://github.com/abetusk/papers
		
		OpenAI Special Projects
		https://news.ycombinator.com/item?id=12181881
		
		Drone Hints
			http://www.firstquadcopter.com/quadcopter-news/inside-syma-x5c-remote-controller/
			https://en.wikibooks.org/wiki/RC_Airplane/RCAP
			http://www.symatoystore.com/Syma-Wholesale
			https://www.youtube.com/watch?v=EQbRnQsHLHA&feature=youtu.be
			http://hackaday.com/2015/09/20/hacking-2-4ghz-radio-control/
			http://hackaday.com/2014/12/10/reverse-engineering-the-proto-x-quadcopter-radio/
			
			
		Ceiling Fan Hacking
		http://hackaday.com/2016/07/04/emulating-a-remote-control-ceiling-fan-transmitter-in-an-fpga/
		
	8.2
		https://www.openhardware.io/
		
		BosLab Crowdfunding
		https://www.generosity.com/community-fundraising/molecule-for-treating-age-related-diseases--2
		
		
		Capitalism slides	https://docs.google.com/presentation/d/1zQG585cbuoMAn482hxR1GZtLKa16Qy_3QltIotXkSKg/edit#slide=id.g15e44de12f_0_258
		
		
		GIFs in matplotlib
		http://eli.thegreenplace.net/2016/drawing-animated-gifs-with-matplotlib/
		
		
	8.8
	
		Great example IPython notebooks
		https://github.com/minimaxir/movie-gender/blob/master/movie_gender.ipynb
		https://github.com/minimaxir/stack-overflow-survey/blob/master/stack_overflow_dev_survey.ipynb
		
		Wonks at Hudson Institute, discuss secular stagnation
		http://www.hudson.org/events/1356-are-plutocrats-drowning-our-republic-72016
		
	8.9
	
		Packet transmission for Syma X11
		https://github.com/goebish/nrf24_multipro
		
			RF24
			http://playground.arduino.cc/InterfacingWithHardware/Nrf24L01
			
			explained a lot better
			https://github.com/bradquick/bradwii
			
				https://github.com/search?utf8=%E2%9C%93&q=Multi-Wii
		
		
		Nice! Drone page
		https://altax.net/
		
			the dude
			https://github.com/alduxvm
			
			Drone in the Lab
			https://youtu.be/k6tswW7M_-8
		
			Low latency Rpi
			https://altax.net/blog/low-latency-raspberry-pi-video-transmission/
			
		Multi-Wii: based off componenets in a Wii
		http://www.multiwii.com/
		
		Open source, join or die
		https://opensource.com/business/16/8/building-career-open-source
		
	8.10
	
		Brain Chu, insightful UC Berkley CS student
		"Deep learning has succeeded tremendously with perception in domains that tolerate lots of noise (audio/visual). Will those successes continue with perception in domains that are not noisy (language) and inference/control, which the article touches on? ..." - https://news.ycombinator.com/item?id=12254801
		
		http://www.brianchu.com/
		
	8.16
	
		ML guy with 8-part python tutorial
		http://www.johnwittenauer.net/tensorflow-openai-and-the-state-of-open-source-ml/
		
	8.19
	
		 "One’s horror at appeals for interaction is clearly the consequence of the hundreds of preceding interactions rather than anything specific to the latecomer. "
		 
	 8.23
	 
		New Freddies?
			http://freethoughtblogs.com/hetpat/
			Will Shetterly blog
			Kevin Drum at Mother Jones
			
		Hot Hand review of the Lit: Now with positive findings
			http://nymag.com/scienceofus/2016/08/how-researchers-discovered-the-basketball-hot-hand.html		
		Drone innovators on tech review
		
			skydio, adam bry: https://www.technologyreview.com/lists/innovators-under-35/2016/inventor/adam-bry/
			
			airware, jonathan downey
			https://www.technologyreview.com/lists/innovators-under-35/2016/visionary/jonathan-downey/
			
			
			
		 Drop-Seq, transcriptome for each cell
		 http://mccarrolllab.com/dropseq/
		 
		 
		 Richard Mueller MWP / Soon and Balinaus vs MBH in TechReview
		 http://muller.lbl.gov/TRessays/23-MedievalGlobalWarming.html
		 
		 Nibiru, Nemesis, and Planet Nine
		 https://en.wikipedia.org/wiki/Nibiru_cataclysm
		 
	 8.25
	 
		 Ralph Peters - Constant Conflict. Army College Quarterly, 1997
		 Information assymetry and its role in clash of civilizations
		 http://strategicstudiesinstitute.army.mil/pubs/parameters/articles/97summer/peters.htm
		 
			American culture is criticized for its impermanence, its "disposable" products. But therein lies its strength. All previous cultures sought ideal achievement which, once reached, might endure in static perfection. American culture is not about the end, but the means, the dynamic process ... All previous cultures, general and military, have sought to achieve an ideal form of life and then fix it in cement. Americans, in and out of uniform, have always embraced change (though many individuals have not, and their conservatism has acted as a healthy brake on our national excesses). American culture is the culture of the unafraid.
			
			next up - Fighting for the Future: Will America Triumph?
			
	8.29
	
		For ages now, I've been telling people that the best best code, produced by the most experienced people, tends to look like novice code that happens to work --- no unnecessary abstractions, limited anticipated extensibility points, encapsulation only where it makes sense. "Best practices", blindly applied, need to die.
			https://news.ycombinator.com/item?id=12377385
			
		"It took me four years to paint like Raphael, but a lifetime to paint like a child." - Picasso
		
		
		http://tranquilmonkey.com/hunter-s-thompsons-extraordinary-letter-on-finding-your-purpose/
		
		The man in the saloon steamer has seen all the races of men, and he is thinking of the things that divide men — diet, dress, decorum, rings in the nose as in Africa, or in the ears as in Europe, blue paint among the ancients, or red paint among the modern Britons. The man in the cabbage field has seen nothing at all; but he is thinking of the things that unite men — hunger and babies, and the beauty of women, and the promise or menace of the sky. -Chesterton
		
	9.1
	
		Literate Programming, critique
		http://johnwshipman.blogspot.com/2016/02/is-literate-programming-harmful.html
		
	9.2
	
		This is what an artist's site looks like
		http://www.ltengy.com/dailyhoney/
		
		Argues well on HN
		https://news.ycombinator.com/threads?id=massysett
		 
	9.12
	
		Iranian(?) but writes like Moldbug
		https://news.ycombinator.com/threads?id=eternalban 
		
		Dan Luu, learning to program, other links at the bottom
		http://danluu.com/learning-to-program/
		
	9.13
	
		If you're like me, your impersonations are more than just bad. They're like alter someone's opinion of you permanently for the worse type bad[2]. "That guy has poor judgement" might be spoken confidently by a witness, even if moments before they had been a longtime neutral aquaintance. And not in the sense of politically distateful or even a socially ill-timed jest, simply the poorest execution in emulating the accent, cadence, body-language or any meaningful characteristic of the desired target.

		And so, if you're like me, you know the secret adulation that hides behind your chuckles while listening to a naturally gifted impressionist hold court. And we're not talking about celebrity impressions, just that friend of yours that can caricature your other friends so well, that teacher you both had in 10th grade, his Portugese grandmother - who you've never met but feel like you know at least as well your own based on her catch phrases. 

		At first it's the tightrope walker's amazement: look at him up there avoiding the natural inclination to move his mouth the safe and predictable way we've all been taught to move it[0]. Now he's going to try another sentence, will he finally stumble? But no, he does not, and even if he were to, it's becoming increasing clear there are larger reasons than that he belongs up there and you belong down here - with the chucklers.

		You start to wonder about those reasons - what is it that he *sees* differently up there? Is the world more vivid, is the social landscape more explicitly laid out in an auditory color you're blind to? And what type of stains do you carry on yourself, if he were to turn the blacklight on you.

		And finally and most devastatingly you start to fantasize: If you could do that Mick Jagger as well as him, would you not... go with it, or at least keep it on for a night. Sure change it so it's not a blaringly obvious celebrity, but if you can be anybody why not take advantage sometimes? But he doesn't overdo it like you would, showing his complete modesty and comfortability in his own skin, even under [1] temptation.

		And the final tally: He's not only the one that has the artist's hands, and the artist's eye, but completely lacks the artist's frustration and restlessness. In fact he has now transferred that creative lust onto you, with your impotence to be anybody except what a life of blind habits and anxieties has molded you into.


		[0]:accustomed
		[1]: severe, manifest
		[2]: acts of cowardice

	 9.14
		Thoreau's last paragrpah
		http://thoreau.eserver.org/thelast.html
		
			he needed to find a way to bring his book to an end without arriving at any final conclusion, needed to find a way to leave the inquiry not only tentative but also open-ended and continuing...essential to Transcendentalism, which was, very briefly, the insistence always on leaving off with matters still very open-ended and unclosed. 
			
			
		“If you want to build a ship, don’t drum up people together to collect wood and don’t assign them tasks and work, but rather teach them to long for the endless immensity of the sea.” - Antoine de Saint-Exupéry
		 
		 The Fall Classic
		 https://en.wikipedia.org/wiki/Ten_Cent_Beer_Night
		 https://www.youtube.com/watch?v=LzWVDyqTolI
		 
		 
	 9.19
	 
		Joel on Camrbirdge in Springtime, a lament for P Greenspun's 90's website
		http://www.joelonsoftware.com/articles/fog0000000021.html
		
	9.20
	
		Reasonable right-center Commenter, Craig
		https://www.allthink.com/craggbragg
		
		What I remember most about September 11th was for looking to others for a response. What would the grown-ups do? What pores would temporarily flare open in the authority structures and would we see the secret M.O. inside it?
		
		First week fof high school, low man on the totem pole, but also the most hopeful and wide eyed.
		
		Canada rape case
		https://www.allthink.com/1531958
		
		James Miller's (econ @Smith) podcast
		https://soundcloud.com/user-519115521
		
		GKC - essays
		http://essays.quotidiana.org/chesterton/lying_in_bed/
		http://essays.quotidiana.org/chesterton/running_after_ones_hat/
		
	9.21
	
		SnowCrash thought - converted office parks to residential like the Walter Baker chocolate factory. But who would want that?
		
	9.22
	
		Ping Pong bowling trick shots
		https://www.facebook.com/9gag/videos/10154971329201840/
		
		
		John Novak, recreational (graphics) programmer
		http://blog.johnnovak.net/about/
		
		
		Indico, Hello MNist
		https://indico.io/blog/simple-practical-path-to-machine-learning-capability-part3/
		https://news.ycombinator.com/item?id=12557212
		
		Robot + ImgProc HelloWorld by Oreilly
		https://www.oreilly.com/learning/how-to-build-a-robot-that-sees-with-100-and-tensorflow?twitter=@bigdata
		
		https://www.hotjar.com/blog/the-passion-fallacy
		
			If you want to succeed – you essentially want a 1% lifestyle. You want to live a life that only 1% of the population can afford to live. That means you need to work harder and smarter than the 99% – who are aspiring to do the same thing.
			
			
		One Second After, EMP scenario fiction
		https://www.amazon.com/Second-After-John-Matherson-Novel/dp/0765356864
		
		
	9.26
	
		Stroke at 26, HN discusses how to chill the fuck out
		http://www.nytimes.com/2016/09/25/jobs/what-i-learned-from-a-stroke-at-26-make-time-to-untangle.html
		https://news.ycombinator.com/item?id=12577685
		
			Hustle, a biz self help book
			http://www.goodreads.com/book/show/31376178-hustle
		
		Victor Ho, Managment/Career advice	http://www.nytimes.com/2016/09/25/business/victor-ho-of-fivestars-take-management-advice-from-interns.html
		
		HN discussion of FIRE vs Mainstreet economic model
		https://news.ycombinator.com/item?id=12577005
		
		dotnet standard
		https://blogs.msdn.microsoft.com/dotnet/2016/09/26/introducing-net-standard/
		
		IBM swift sandbox
		https://swiftlang.ng.bluemix.net/#/repl
		
	9.28
	
		HAckerRank, tutorials: python and ai
		https://www.hackerrank.com/domains?h_r=logo
		
			https://www.hackerrank.com/domains/tutorials/cracking-the-coding-interview
			
		Open AIs
		https://openai.com/blog/team-plus-plus/
		
		
	10.3
	
		Five minutes to Live (Sermon)
		https://rabbiedbernstein.files.wordpress.com/2016/10/five-minutes-to-live-rabbi-kenneth-berger-z22l-yom-kippur-sermon-sept-1986.pdf
		
		Four steps to epiphany
		http://web.stanford.edu/group/e145/cgi-bin/winter/drupal/upload/handouts/Four_Steps.pdf
		
		3,2,1
		
	10.4 
	
		Psychopath Code, Hitjens
		
		It was in Culture & Empire that I began writing on psychology. My expertise, and what fascinates me, is social psychology. That is, how groups work, and how people work within groups. It is the core of my work in open source community building. Software is all about people, it turns out.
		
		
		Social Architecture, Hitjens
		TIP: One free contributor is worth 10 paid contributors.

		
	10.5
	
		Goodhart's Law: "When a measure becomes a target, it ceases to be a good measure."
		
		Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes.
		
		Goodhart's original 1975 formulation:
			A risk model breaks down when used for regulatory purposes.
			
			
		Book of 20th centruy American Inventors
		http://www.wsj.com/articles/kevin-baker-america-the-ingenious-1475614748
		
		Data Exchange
		
		http://www.dataexchangellc.com/
		
		http://www.buzzfile.com/business/Data-Exchange-LLC-908-342-1633_no:15189919
		
			Also in Rochester, NY
			http://www.buzzfile.com/business/Data-Exchange-LLC-585-750-7572
			
			Got like 6 followers
			https://twitter.com/RethnkIT
			
				
			
				Chris Dutra
				https://github.com/dutronlabs
				
				
				https://apprenda.com/
					https://twitter.com/Apprenda   12K followers
					https://www.linkedin.com/in/dutrachr
		
		The Pulse Network
		http://www.tpni.com/
		
		TEDx Springfield @massmutual (2015)
		http://www.masslive.com/news/index.ssf/2015/10/tedxspringfield_brings_ideas_l.html
		
	10.11
	
		RPi Home automation blog
		https://jacklew.is/raspberry-pi-door-opener/
		
		
		Dennett, these words don't actually exist
		https://ase.tufts.edu/cogstud/dennett/papers/Chapter_5.pdf
		
	10.12
	
		
		
		Discussion on sqlserver express image
		https://news.ycombinator.com/item?id=12690853
		
			CALS
			https://www.microsoft.com/en-us/licensing/product-licensing/client-access-license.aspx
			
			enterpriseDB, redhat for postgres			
			http://forums.enterprisedb.com/posts/list/1678.page
		
		
		Using the rpi as a microcontroller
		https://ultibo.org/make/
		
	
		The sacred, and how religious entrepreneurs create it	https://theviewfromhellyes.wordpress.com/2014/11/27/sacredness-as-practiced-by-religious-entrepreneurs-rape-riots-and-economic-efficiency/?utm_content=bufferb2e62&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer
		
			old: http://theviewfromhell.blogspot.com/2011/03/russian-dolls.html
		
		AWS open guide
		https://github.com/open-guides/og-aws#aws-data-transfer-costs
		
		Deep Learning school
		https://www.youtube.com/watch?v=eyovmAtoUx0
		
		
	10.13
	
		Tube Talk - get londoner to talk on subway	http://www.wsj.com/articles/londons-most-persistent-american-will-not-quit-until-tube-riders-talk-to-each-other-1476364466
		
		Deep Mind uses structured knowledge in AI
		https://deepmind.com/blog/differentiable-neural-computers/
		
		
	10.17
	
		Hello, I'm Peter Thiel, and I'm a libertarian
		https://www.cato-unbound.org/2009/04/13/peter-thiel/education-libertarian
		
		
		AvenueIngres, SSC-esque
		https://news.ycombinator.com/threads?id=AvenueIngres
		
		Another informed commenter
		https://news.ycombinator.com/threads?id=Turing_Machine
		
		Doing .Net on Linux
		http://piotrgankiewicz.com/2016/10/17/net-on-linux-bye-windows-10/
		
		
		David Wong books, hes editor of cracked.com
			https://www.amazon.com/Brief-History-Vice-Behavior-Civilization/dp/0147517605
			https://www.amazon.com/Futuristic-Violence-Fancy-Suits-David/dp/1250040191
			
		Ana Liu, Media Lab
		http://ani-liu.com/hello
		
	10.19
	
		Waitstaff webcomic
		http://bigbigtruck.deviantart.com/art/A-Year-In-Waiting-8-118699878
		
		Jose, PHP dev, big on github
		http://josediazgonzalez.com/2016/01/26/open-source-is-hard/
		
		On TDD:
		The conversation around TDD is tired, and the conclusion is always the same: "it depends." It depends on the person writing the code, the type of problem they're tackling, the language they're using, the needs of the business, etc.
		This study doesn't bring anything new to the table except: "in this manufactured environment we found a single point of data that equates to noise."
		
		Finance to Dev
		http://ericdykstra.me/blog/intro
		http://ericatdbc.tumblr.com/archive
		
		
	10.20
	
		Learn VBA	https://mva.microsoft.com/en-US/training-courses/visual-basic-fundamentals-for-absolute-beginners-16507?l=b9HXBTKbC_6706218965
		
		.suo files explained
		https://github.com/ParticularLabs/SetStartupProjects
		
			Open MCDF - to manipulate .suo files
			http://openmcdf.sourceforge.net/
			
		Ye Olde VS - Macros and breakpoints	http://stackoverflow.com/questions/841782/programmatically-apply-deactivate-breakpoints-in-visual-studio?rq=1
		
		Debug.Assert   - interesting
		https://msdn.microsoft.com/en-us/library/system.diagnostics.debug.assert.aspx
		
			The System.Diagnostics.Debug Class
			https://msdn.microsoft.com/en-us/library/system.diagnostics.debug(v=vs.110).aspx
			
		Taxonomy of NN
		http://www.asimovinstitute.org/neural-network-zoo/#
		
		.net core tooling
		https://news.ycombinator.com/item?id=12750068
		
		
	10.21
	
		GAC - explanation
		https://msdn.microsoft.com/en-us/library/yf1d93sz.aspx
		
		Troubleshooting
			http://stackoverflow.com/questions/810203/the-following-module-was-built-either-with-optimizations-enabled-or-without-debu
			https://forums.asp.net/t/996830.aspx?The+following+module+was+built+either+with+optimizations+enabled+or+without+debug+information
			
	10.24
	
		Gender in policy making
		https://lawfareblog.com/beyond-grabbing-gender-conflict-and-national-security-establishment
			illutrates the problem with "the conversation on gender" as it used today: it is used for showmanship to sell policymakers / policy but refuses to acknowledge the reality that gender plays in policy outcomes
		
		Example of a technichally correct, but actually it should be the opposite:
			Now that Tesla is making cars with all the hardware to self-drive, but don't have the software yet, it could be technichally said that the software is the thing that we haven't been able to develop. But if you look at 2005, we had the hardware already - lidar and digital cameras, the big question was could anyone build software like that. Now we know we can which is the true breakthru although the hardware team could say they delivered first.
			
		Ed Woo Policing DIYbio	https://www.technologyreview.com/s/602643/on-patrol-with-americas-top-bioterror-cop/?utm_campaign=content-distribution&utm_source=dlvr.it&utm_medium=twitter
		
		List of games on github
		https://github.com/leereilly/games
		
		MSDN, using AZure for EHR's
		https://msdn.microsoft.com/en-us/healthvault/dn783322
		
		Reality is broken, games make us better
		https://www.goodreads.com/book/show/7821348-reality-is-broken
		
	10.27
	
		Git primers
		https://codewords.recurse.com/issues/two/git-from-the-inside-out
		
			http://stackoverflow.com/questions/927358/how-to-undo-last-commits-in-git#927386
			
			https://github.com/tj/git-extras
			
			https://jwiegley.github.io/git-from-the-bottom-up/
			
		
		Job Search Spreadsheet	http://kellysutton.com/2016/10/20/visualizing-a-job-search-or-how-to-find-a-job-as-a-software-engineer.html
		
	10.28
	
		Holly Woodland's crowd paper
		http://www.nature.com/articles/ncomms12846
		
		
		Cool! Python Word2Vec sourceCode recommender systems
		https://gab41.lab41.org/python2vec-word-embeddings-for-source-code-3d14d030fe8f#.l41lsb7fb
		
		Recommender systems datasets
		https://github.com/lab41/hermes
		
		How to learn about ML / AI
		https://news.ycombinator.com/item?id=12817426
		
		comma ai
		https://github.com/commaai/research
		
		Kyle Russell, would prolly like the PPD
		https://twitter.com/kylebrussell
		
		Build AI algos?
		http://www.vicarious.com/
		
		Tyson Chandler, bullying
		http://www.theplayerstribune.com/bullying-awareness-tyson-chandler/
		
	10.31
	
		Python AsyncIO writeup
		https://news.ycombinator.com/item?id=12829759
		
		SLides on Entrepreneurship
		https://news.ycombinator.com/item?id=12834804
		
		HackerNews Dataset
		http://aaron-hoffman.blogspot.com/2016/10/hacker-news-dataset-october-2016.html
		
		Drone in the picture is the one to get
		https://www.technologyreview.com/lists/innovators-under-35/2016/visionary/nora-ayanian
		
		Aaron Hoffman, MS open source guy
		https://github.com/stonefinch/
		
			Azure intro
			https://github.com/Stonefinch/AzureIntro
		
		I would say 3 options to be able to bareboat charter: 1) take ASA or US Sailing courses up to bareboat cruising 2) go with someone who owns or can charter a boat 3) Crew boats and sail smaller boats and work your way up. I went the first route, I have the US Sailing certifications up to Bareboat cruising

		C# / Product Manager job
		http://stackoverflow.com/jobs/126169/freeform-product-engineering-manager-3d-systems-inc
		
		
	11.1
	
		WP on AWS, breif guide on scaling to 2 vm's
		https://cloudonaut.io/wordpress-on-aws-smooth-and-pain-free/
		
		Stupid Drone as a ball kickstarter
		https://www.kickstarter.com/projects/zyro/zyrotm-droneball
		
		Parrot-mini can carry a pingpong ball	http://www.theaustralian.com.au/life/personal-technology/parrot-mambo-ferries-letters-swing-is-half-drone-half-plane/news-story/49109fd45dd2a3439811f8377ddc17db
		
		Writeup of PPD
		http://researcher.watson.ibm.com/researcher/view_group_subpage.php?id=6569
		
		WindowTypes for VS Extensions
		https://msdn.microsoft.com/en-us/library/envdte.vswindowtype.aspx
		
		PubPub - Sci publishing 2.0
		https://www.pubpub.org/pub/hello
		
		Music for Programming
		https://www.brain.fm/app#!/player/35
		
			https://news.ycombinator.com/item?id=12844434
		
	11.2
	
		Jaeger @WPI, does robotics, looking for job
		https://news.ycombinator.com/user?id=amjaeger
			https://news.ycombinator.com/item?id=12846711
			http://users.wpi.edu/~amjaeger/
		
		
		Visual SLAM person
		https://news.ycombinator.com/user?id=devin_lane
			https://news.ycombinator.com/item?id=12849381
			
			nice c++ example for CV
			https://shiftedbits.org/2011/01/30/cubic-spline-interpolation/
		
		
		Dockwa app for marina reservation, 
		https://dockwa.com/
		
			they are hiring
			https://news.ycombinator.com/reply?id=12847326
		
		You described your guantanamo fever dreams, I say it's already happening	https://www.washingtonpost.com/opinions/global-opinions/venezuela-is-holding-our-son-hostage-and-the-us-doesnt-seem-to-care/2016/11/02/a8624224-9a34-11e6-9980-50913d68eacb_story.html
		
		debug an rpi in visualstudio - visualgdb
		http://raspberrypi.stackexchange.com/questions/47972/remote-debugging-with-visual-studio-2015
		
	11.3
	
		"If you’re bootstrapped and have an email list of 1,000 people and want to grow that list, you don’t need a full-time email marketing manager, a writer, a designer and a junior marketer to execute on a content marketing strategy for you...You need a motivated, scrappy content marketer who can do all of those jobs at once."
		
		Visual Studio Code
		https://code.visualstudio.com/docs/runtimes/office
		
		Salaries of Cal Employees
		http://transparentcalifornia.com/salaries/search/?q=firefighter&y=
		
		Why functional programming
		http://transparentcalifornia.com/salaries/search/?q=firefighter&y=
		
		The source for VS code
		https://github.com/Microsoft/vscode/wiki/How-to-Contribute#build-and-run-from-source
		
		opencv docs
		http://stackoverflow.com/documentation/opencv/topics
		
	11.7
	
		New Face Detector, Rosenbrock's on-board
		http://blog.dlib.net/2016/10/easily-create-high-quality-object.html
		
		Conversation by Adiran on Py-enabled Drones
		https://twitter.com/PyImageSearch/status/781519330618073089
		
			eg GoPiGo2
			http://www.dexterindustries.com/shop/gopigo-starter-kit-2/
			
			
		
		Rosenbrock repo
		https://github.com/jrosebr1
		
		https://www.bitcraze.io/crazyflie-2/
		
			$180
			https://www.seeedstudio.com/Crazyflie-20-p-2103.html#
		
			oh shit, positioning system
			https://www.bitcraze.io/2016/10/loco-positioning-system-update-kalman-controller-and-tdma/
				
				so its radio triangulation
				$150 per node
				
			using the flie in univ research
			https://www.bitcraze.io/2016/06/loco-positioning-in-lth-math-department/
			
			adding tiny camera FPV: 1g camera + 2g transmitter + battery
			https://www.hackster.io/fredg/crazyflie-2-0-fpv-setup-d2fc25
			
			Mechanichal stuff
			https://www.bitcraze.io/category/crazyflie/cf-mechanic/
			
			And the code stuff
			https://bitbucket.org/omwdunkley/crazyflie-pc-client-camera
			
			Demo of these, theyre the small ones at the end swarming	https://www.ted.com/talks/raffaello_d_andrea_meet_the_dazzling_flying_machines_of_the_future?language=en
			
			
		Drone purchase
		
			$4 per controller
			http://www.ebay.com/itm/like/281983356256?lpid=82&chn=ps&ul_noapp=true
				
			$19 D63, ebay expires in 3 days	http://www.ebay.com/itm/SYMA-Sky-Thunder-RC-D63-Drone-Runner-2-4-GHZ/232134728279?_trksid=p2141725.c100338.m3726&_trkparms=aid%3D222007%26algo%3DSIC.MBE%26ao%3D1%26asc%3D20150313114020%26meid%3Db4df9459f8934863887116202b54a403%26pid%3D100338%26rk%3D5%26rkt%3D15%26sd%3D281983356256
				
		Desktop wind tunnel
		https://twitter.com/desk_breeze
	
		Robotic Arm
		https://www.hackster.io/Ricky/syncing-robotic-arm-tutorial-a273ab
		
		SuperCam for pingpong		http://www.i-programmer.info/news/192-photography-a-imaging/4630-camera-fast-enough-to-track-ping-pong-balls.html
		
			http://spectrum.ieee.org/automaton/robotics/robotics-hardware/robot-eyes-track-ping-pong-balls
		
		Humanoid Robot plays ping pong. 2011, China
		http://www.i-programmer.info/news/169-robotics/3223-ping-pong-robots.html
		
		
		Research Grade robot arm, research project to teach it (2012)
		https://www.youtube.com/watch?v=SH3bADiB7uQ
		
		Web tech in python
		https://realpython.com/
		
		
	11.8
	
		Cool list of live updates on revenue for small software companies
		http://www.transparentstartups.com/
		
		Many (not all) "art" games tend to end up being kitschy because they're designed to signal and appeal to an elite in-group's values rather than being a true expression of ideas of their own. I think a piece has more artistic merit if it reflects ideas and truths the artist discovered for themselves, - overgard  https://news.ycombinator.com/threads?id=overgard
		
		How to prod security
		https://breaker101.com/
		
		Roomba for bedbugs, etc... co2 emissions + heat, vaccuum collection
		
		Christopher Doyle
		https://twitter.com/MrDataScience
		
		
		Excel-DNA, build C# into Excel
		https://excel-dna.net/
		
		
		from 2013, xamarin + opencv (2.4.4)
		
		yeah, i had solution for this.
		I use OpenCV 2.4.4 on native and write Objective-C static library work with OpenCV. Then, binding this library from C#, you can research with http://docs.xamarin.com/guides/ios/advanced_topics/binding_objective-c_libraries

		When built static library from Objective-C, you will get a .a file, like libSmartImage.a .You also must add OpenCV to binding project from C#, rename file opencv2 in opencv2.framework/Version to opencv2.a

		Overall, you must add two files libName.a and opencv2.a to Binding project of Xamarin.iOS.
		And with opencv2.a file binding, use must add to link file: 
		LinkWith ("opencv2.a", LinkTarget.ArmV7 | LinkTarget.Simulator, ForceLoad = true, IsCxx = true, LinkerFlags = "-ObjC -lz -licucore -lc++", Frameworks="QuartzCore AVFoundation CoreVideo AssetsLibrary CoreGraphics CoreMedia")]

		https://components.xamarin.com/gettingstarted/xpand.opencvbinding
		
		Drone Tracking with optical flow
		https://www.youtube.com/watch?v=C95bngCOv9Q
		
		Ping pong ball balancing
		https://www.youtube.com/watch?v=p65XPP53rLo
			https://github.com/karfly/balanceball
			
			PID math lecture
			https://www.youtube.com/watch?v=0vqWyramGy8
			
			Tune a loop, math lecture
			https://www.youtube.com/watch?v=3viD5ij60EI
			
		http://www.emgu.com/forum/viewtopic.php?t=4690
		focus. If you find that you are not hitting 30 FPS, it may be the camera's auto adjustment system responding to a low light situation. In this case you can disable RightLight using Logitech camera controller software.
		
		probably is windows 8 vs 8.1 
		or x64 vs x86?
		could be python instead of c++
		might not have numpy linear algebra libraries?
		V4L2?
		Try just recording using software
		
		Quadcopter flown by computer, very similiar to my attempts
		https://www.youtube.com/watch?v=_LIBB9qlJoU
		
		Object Tracking, no color, compare img1 to img2
		https://www.youtube.com/watch?v=X6rPdRZzgjg
		
		Quad Test Suite
		http://www.miniquadtestbench.com/
		
		PiZero via USB only!
		http://blog.gbaman.info/?p=791
		
		
		DirectShow with Webcam demo project
		http://www.codeproject.com/Articles/18511/Webcam-using-DirectShow-NET
		
		
		OpenCV3 Blueprints
		https://books.google.com/books?id=tfOoCwAAQBAJ&printsec=frontcover#v=onepage&q&f=false
		
		ScreentoGIF
		http://screentogif.codeplex.com/
		
		
	11.9
	
		Sailboat office guy
		http://www.wsj.com/articles/office-hostage-escapes-to-sail-the-seas-re-creates-office-1478536723
		
		"Ugly, but True" - Nesly on DJT
		
		Gene Wolf, The Book of the New Sun
		https://news.ycombinator.com/item?id=12884413
		
	11.10
	
		CloudRail - put files up to any cloud
		https://cloudrail.com/enterprise-cloud-storage-interface/
		
		Xamarin testomonials - the good and the bad
		https://news.ycombinator.com/item?id=12948611
		
		
	11.15
	
		C++ history, adoption by Bjarne	https://channel9.msdn.com/Events/CPP/CppCon-2016/CppCon-2016-Bjarne-Stroustrup-The-Evolution-of-C-Past-Present-and-Future
		
		DIYbio links
		http://citizensciences.net/biofabbing/
		
		
		SelfDriving Course
		https://www.udacity.com/self-driving-car
		
			https://www.wired.com/2016/09/udacity-self-driving-car-engineer-nanodegree-program-thrun/
		
			Challenge2 - steering angle	https://medium.com/udacity/challenge-2-using-deep-learning-to-predict-steering-angles-f42004a36ff3#.lzkjkj5ju
		
		Teach the computer to do physics experiments via Reinforcement learning
		https://arxiv.org/pdf/1611.01843v1.pdf
		
	11.16
	
		https://aiexperiments.withgoogle.com/
		
			Draw for the neural nets
			https://quickdraw.withgoogle.com/
		
			NN Viz, for Artists
			http://ml4a.github.io/
			
			
		Retro sci-fi, mostly spaceships
		http://imgur.com/gallery/RbV0Q
		
		
		Ping pong ball mouth video
		https://twitter.com/ZooMass/status/798959203784282112
		
		Nice little DataScience blog
		http://techfiction.xyz/
		
		
	11.18
	
		Sabbaday, what a day
		http://www.alltrails.com/explore/trail/us/new-hampshire/sabbaday-brook-trail
		
			The fool killer	http://www.conwaydailysun.com/outdoors/hiking/128-outdoors/other-hikes/107862-parsons-hiking-for-6-29-13
		
		bonhomie vs anomie
		
	11.21
	
		Brian Eno once said that the Velvet Underground’s debut album only sold a few thousand copies, but everyone who bought it started a band. 
		
		You can get an Rpi image from pyimagesearch with openCV already installed
		
		Robot, to teach the kids
		http://www.olin.edu/the-wire/2016/one-little-robot-big-hopes-digital-literacy/
		
		To study for programming interviews
		https://www.interviewcake.com/
		
		
		It's cool, with the kids
		https://chat.meatspac.es/
		
		
		Olin girl, playing ping pong
		https://www.facebook.com/alison.wu?fref=nf
		
		
	11.28
	
		mm-scale indoor position tracking repo
		https://news.ycombinator.com/item?id=13053182
		https://github.com/ashtuchkin/vive-diy-position-sensor
		
			vive lighthouse video https://www.youtube.com/watch?v=oqPaaMR4kY4
				thread:
				https://www.reddit.com/r/Vive/comments/40877n/vive_lighthouse_explained/
				blog:
				http://doc-ok.org/?p=1478
				writeup
				http://gizmodo.com/this-is-how-valve-s-amazing-lighthouse-tracking-technol-1705356768
				
			Players in VR:
			
				ValveSoftware: https://github.com/ValveSoftware
				Etc: http://store.steampowered.com/
				
		
		Teach the kids to code with Instagram and Snapchat
		http://www.vidcode.io/
				
				
		Drones fly hard and accurate
		https://www.youtube.com/watch?v=MvRTALJp8DM		
		
		More from the ibm group
		http://researcher.watson.ibm.com/researcher/view_group_subpage.php?id=6569
		
		Once again, heres the most research you can get from ibm's ping pong drone
		http://researcher.watson.ibm.com/researcher/view_group_subpage.php?id=6569
			it has a link to nall the press ocverage - good resource
			
			
		Guy at Imaging meetup tomorrow
		http://www.firstshotlogic.com/
		
		
		The old pitch theme
		https://wordpress.org/themes/pitch/
		
	
	11.30
	
		"I wonder about it all" Anti-Communist in Cuba	http://www.dailymail.co.uk/news/article-3984170/KATIE-HOPKINS-came-Cuba-commie-hater-ready-bury-Castro-ended-praising-dictator-people-ways-freer-are.html
		
		
		Beirut on the Wall
		https://www.facebook.com/OchePong/
		
		Interesting guy
		https://news.ycombinator.com/threads?id=throwanem
		
	12.2
		
		How a Video becomes a virus
		https://googleprojectzero.blogspot.com/2016/06/how-to-compromise-enterprise-endpoint.html
		
		Linux on Windows how to guide
		https://nickjanetakis.com/blog/create-an-awesome-linux-development-environment-in-windows-with-vmware
		
		
	12.5
	
		Siraj, makes YT vids for hacker news, laundry folding robot?
		https://news.ycombinator.com/user?id=llSourcell
		https://www.youtube.com/watch?v=mGYU5t8MO7s
		
		OpenAI Universe
		https://news.ycombinator.com/item?id=13103742
		\https://universe.openai.com/
		
			How to add your own game as an environment
			https://news.ycombinator.com/item?id=13105834
		
		
		Conservative Canadian Journal
		http://www.c2cjournal.ca/2016/12/the-new-campus-rebels-c2c-journals-winter-2016-edition/
		
		
		MediaWiki A Wiki Template
		https://www.mediawiki.org/wiki/MediaWiki
	
	
	12.6
	
		NPR Best Books
		https://apps.npr.org/best-books-2016/#/_
		
		Bill Gates Best Books
		https://www.gatesnotes.com/About-Bill-Gates/Best-Books-2016?linkId=31806383
		
		
		Drone Software guy
		https://news.ycombinator.com/threads?id=nzjrs
		
		DIY hardware thread
		https://news.ycombinator.com/item?id=13108432
		
	12.7
	
		VBA tools, 
		https://github.com/VBA-tools
		
			JSON parser - also a well written VBA workspace
			https://github.com/VBA-tools/VBA-JSON
			
			Made by Tim hall, a plastics engineer
			http://timhall.github.io/
			https://www.linkedin.com/in/timhallengr
			
				His day job, d3-ing
				e.g. http://csnw.github.io/d3.compose/examples/#/lines-and-bars
				
		
		20 Most Creative People in LifeInsurance
		http://www.lifehealthpro.com/2015/07/29/the-20-most-creative-people-in-insurance?t=life-insurance
		
			http://lifetrends.com/
			Flirting with Welis, Karen Joyner, David Lear. Based in Austin.

			Buy term with UW questions
			https://www.policygenius.com/life-insurance/comparison
				
				Team of millenials
				https://www.policygenius.com/about/team
			
					Brooklyn man works in insurance
					https://github.com/PepperTeasdale
					
				Timeline, 2013 - present
				https://www.policygenius.com/careers
				
				
			HavenLife an MM direct sale
			https://havenlife.com/#quickquote
			
			Compare HealthInsurance reimburments
			https://www.healthpocket.com/
			
			"past results do not predict future performance"
			
			Maria Umbach is now Maria Ferrante-Schepis
			
			NFP
			http://nfp.com/
			https://www.linkedin.com/company/wearenfp
	

		Free code camp produces a million medium blogs
		https://medium.freecodecamp.com/about
		
		SALTO, jumping robot
		http://spectrum.ieee.org/automaton/robotics/robotics-hardware/uc-berkeley-salto-is-the-most-agile-jumping-robot-ever
		
		Robot foosball
		http://spectrum.ieee.org/automaton/robotics/robotics-hardware/video-friday-robo-foosball-fetch-snackbot-and-europa-submarine
		
		Lego drone kit - the Wrong borthers
		http://spectrum.ieee.org/automaton/robotics/robotics-hardware/lego-drones-robots-in-the-desert-pepper-new-tricks
		
		
		Product Hunt
		https://www.producthunt.com/
		
		
		Java for pythonista
		http://interactivepython.org/courselib/static/java4python/Java4Python.html
		
		
	12.8
	
		"Have you ever known anybody to turn away from anything they found compulsively engaging? We don’t decide about life; we’re captured by life. In the major spheres, decision-making, when it happens at all, is downstream from curiosity and engagement. If we really want to understand and shape behavior, maybe we should look less at decision-making and more at curiosity." -D Brooks
		
			-> Jobs and Education reform
			
		https://istacee.wordpress.com/
		C# dev blog
		
		
		ToggleBoggle, a mensch
		http://togglesbloggle.tumblr.com/
		
			Getting into poetry
			http://togglesbloggle.tumblr.com/post/153154511758/nihilsupernum-i-am-interested-in-getting-into
			
		Turing's the chemical basis of morphogenesis
		http://www.dna.caltech.edu/courses/cs191/paperscs191/turing.pdf
		
		
	12.9
		http://stackoverflow.com/questions/16744863/connect-to-amazon-ec2-file-directory-using-filezilla-and-sftp
		
	12.12
	
		Excel for Python
		http://docs.python-tablib.org/en/latest/
		
	12.13
	
		HN dicusees the purpose of evolution
		https://news.ycombinator.com/item?id=13161587
		
		Surpirse, python recommendation
		https://news.ycombinator.com/item?id=13131149
		
		
		Actuaries in healthcare
		https://www.statnews.com/2016/12/13/actuaries-health-care-precision-medicine/
		
	12.15
	
		Insurance in the news	http://www.nytimes.com/2016/12/09/your-money/combine-long-term-care-with-life-insurance-do-the-numbers-first.html	http://www.nytimes.com/2016/12/09/business/dealbook/wells-fargo-accusations-sham-insurance-policies.html?mabReward=A5&recp=1
		
		Statistics show crime is most often committed by men of a certain age; old enough to break the rules but too inexperienced to appreciate the consequences.
		
		
	12.19
	
	
		What now, 2001 responses to 9/11
		https://www.edge.org/responses/what-now-
		
			idiotic - airplane tech
			most cogent - https://www.edge.org/response-detail/11267
				get u.s. out of s.a., allows islamist take over of s.a., oil money buys nukes, nukes reset both side to mideivel level of tech and society
				
	12.20
		
		Adverserial Models GAN, an ML technique
		http://www.kdnuggets.com/2016/07/mnist-generative-adversarial-model-keras.html
		
		People tweeting about robots, but its just a scam
		https://twitter.com/hashtag/MyCustomizedRobot
		
		Rocket Scientist know-it-all
		https://www.youtube.com/watch?v=c0a7eR8Wi4Y
		
		
		Jeremy Howard's 6pt kaggle/aws based deep learning class
		http://course.fast.ai/
		
			HN: https://news.ycombinator.com/item?id=13224588
				jeremy: https://news.ycombinator.com/user?id=jph00
				
			Their blog:http://www.fast.ai/2016/10/08/teaching-philosophy/
				
			repo: https://github.com/fastai/courses/tree/master/deeplearning1/nbs
		
			Student examples:
				radio signal denoising https://arxiv.org/pdf/1602.04105.pdf
				
			lectures:
				lesson1:https://www.youtube.com/watch?v=Th_ckFbc6bI&feature=youtu.be
				lesson0:
				setup aws:https://www.youtube.com/watch?v=8rjRfW4JM2I
				
				
				
			Related:
				you should know the math opinion: http://www.inference.vc/deep-learning-is-easy/
				another course for beginners to apply: https://www.kadenze.com/courses/creative-applications-of-deep-learning-with-tensorflow/info
				hes "2nd" in the udacity self driving car course: https://news.ycombinator.com/user?id=cr0sh
				plankton kaggle winner explains: http://benanne.github.io/2015/03/17/plankton.html
				
				
		Women inventor of wireless power, uBeam
		http://mobile.nytimes.com/2013/08/18/technology/an-inventor-wants-one-less-wire-to-worry-about.html
				
		
		A Learning and Development engineering consultants for software defined radio
		http://corganlabs.com/
		
		 “good fences make good neighbors,” and one of the virtues of the Westphalian approach to state sovereignty is that it established clear boundaries and made infractions easier to spot. These features didn’t make war impossible, of course, but they made it easier to identify clear acts of aggression and made it less likely that states would stumble into war because they had crossed some unknown tripwire by accident. As norms of sovereignty have eroded and the tools for interfering in other states have become more numerous and sophisticated, states have more reason to fear that others will tamper with their internal politics and the danger of mutually reinforcing, tit-for-tat spirals goes up. 
	 
	 12.27
		 
		 https://news.ycombinator.com/item?id=13259429
		
		Deep Learning guide
		http://yerevann.com/a-guide-to-deep-learning/
		
		
	1.3
	
		Mensch
		http://davidauerba.ch/
		http://www.waggish.org/
		
		Yes but labor rights is a poor substitute for a system that allows and encourages small business. I'm not talking about "Entrepreneurs" in the new sense of the term, I'm talking about the sense that the first 200 years of America fostered, where basically after apprenticeship any tradesman started their own firm and became their own boss.
		Labor rights are a bad consolation prize for a system that should be encouraging self determination.
		
	1.4
		
		VideoGame with AI
		https://github.com/kevinhughes27/TensorKart
		http://kevinhughes.ca/blog/tensor-kart
		
		side proj advice
		https://dev.to/liquidise/side-projects---avoiding-failures-to-launch
		
		Fleye, worlds safest drone, on kickstarter
		
	1.6
		
		Deep work, no distractions
		https://www.amazon.com/Deep-Work-Focused-Success-Distracted-ebook/dp/B00X47ZVXM?tag=leavethegreat-20
		
		Let the kids work
		https://fee.org/articles/let-the-kids-work/
		
		Poker AI
		http://www.cmu.edu/news/stories/archives/2017/january/poker-pros-vs-AI.html
		
		Cool numpy primer
		http://www.labri.fr/perso/nrougier/from-python-to-numpy/
			
			github publishing tools here:
			https://github.com/rougier/from-python-to-numpy
		
		Good opinion piece on bigdata, ai, and how to use blockchain. reminds me of me
		https://blog.bigchaindb.com/blockchains-for-artificial-intelligence-ec63b0284984#.mmlt0xy3n
		
		Sodoku solver, approach by two programmers, TDD vs Genius
		http://ravimohan.blogspot.in/2007/04/learning-from-sudoku-solvers.html
		
			https://en.wikipedia.org/wiki/Constraint_satisfaction
		
	1.9
	
		Ira glass on the beginners curse
		https://www.goodreads.com/quotes/309485-nobody-tells-this-to-people-who-are-beginners-i-wish
	
	1.11
	
		MIT online course for self driving and deeplearning
		http://selfdrivingcars.mit.edu/
		
		Guy who understands science, quiets the sensationalism
		https://news.ycombinator.com/threads?id=jcranmer
		
			recommended, mol bio blog http://blogs.sciencemag.org/pipeline/
			
			
		9 hours of excel scrolling
		http://9gag.com/tv/p/a3Opzo/over-9-hours-bottom-of-excel?ref=fbl9
		
		Drone day, May 6th Boston. Drydock
		http://dronedayboston.com/
		
		Drone store
		http://www.modelaircraft.org/
		
	1.12
	
		DotNet dev blog
		http://miniml.ist/dotnet/explaining-dotnet-standard-like-im-five/
		
			http://miniml.ist/dotnet/2016-year-in-review/
			
	1.13
	
		cough sci-hub.cc cough
		https://sci-hub.ac/
		
		https://www.kaggle.com/c/data-science-bowl-2017
		
		
		
		Old Kaggle firends
			https://www.kaggle.com/chipmonkey
			http://happytechnologist.com/
			
		Crazy tech youtube guy, Q learning
		https://www.youtube.com/watch?v=A5eihauRQvo&feature=share
		
		
		Biology + AI article	http://www.economist.com/news/science-and-technology/21713828-silicon-valley-has-squidgy-worlds-biology-and-disease-its-sights-will
		
			Niven Narain of BERG Health, an AI and biotechnology firm in Framingham, Massachusetts
			
			
		Recommended thinker by James Miller: https://dominiccummings.wordpress.com/
			
			Much of politics involves very similar tragi-comic scenes re-created by some of the basic atoms of human nature – fear, self-interest and vanity. The years, characters, and contexts change, the atoms shuffle, but the stories are the same year after year, century after century. Delusions and vanity dominate ‘rationality’ and ‘public service’
		
	1.19
	
		Deep Learning Diagrams
		https://medium.com/@gokul_uf/the-anatomy-of-deep-learning-frameworks-46e2a7af5e47#.te3q20zb3
		
		
		https://simonpenner.tumblr.com/post/155662231436/on-unconstrained-use-of-social-power-and-the
		
		Flourp protein viz
		http://www.fpvis.org/
		
		The guy doing python2.8 is awesome
		https://www.naftaliharris.com/blog/2x-speedup-with-one-line-of-code/
		
		
		diy self driving remote control car
		???
		
		neontaster-esque commenter
		https://news.ycombinator.com/threads?id=fdschoeneman
		
		
	1.29
		
		Denoisers not discriminators, gradient diagrams	http://www.inference.vc/variational-inference-using-implicit-models-part-iv-denoisers-instead-of-discriminators/
		
		
	2.1
	
		RL in robotics primer	https://vmayoral.github.io/robots,/ai,/deep/learning,/rl,/reinforcement/learning/2016/07/06/rl-intro/#rrlchallenges
		
		
		AI poker thread
		https://news.ycombinator.com/item?id=13534778
		
		
		Intex, fixed income software on 128
		http://www.intex.com/main/company_careers.php
		
		Morse robotics, a local firm
		http://www.morse-corp.com/jobs.html
		
		FDA seeks to regulate DIYbio
		http://gizmodo.com/the-fda-is-cracking-down-on-rogue-genetic-engineers-1791760888
		
		nuTonomy internship in cambridge
		http://nutonomy.com/jobs.html?gh_jid=472603&gh_src=f75mb21
		
		
		2.13
		
		China drone swarm
		https://www.suasnews.com/2017/02/chinese-one-thousand-drone-swarm-smashes-intel-record/
		
		autodidact analysis of middle east circa2003
		http://russilwvong.com/future/mideast.html
		
		.net 15th anniversary thread
		https://news.ycombinator.com/item?id=13641386
		
		ID-ing browsers	https://arstechnica.co.uk/security/2017/02/now-sites-can-fingerprint-you-online-even-when-you-use-multiple-browsers/
		
		Tickets
		https://news.ycombinator.com/item?id=13643045
		https://motherboard.vice.com/en_us/article/the-man-who-broke-ticketmaster
		
			Why wiseguys werent illegal
			https://www.scribd.com/document/338935972/Wiseguy-Hearing
			
		Rosenbrocks kickstarter	https://www.kickstarter.com/projects/adrianrosebrock/deep-learning-for-computer-vision-with-python-eboo
		
		DIYRoboCars
		https://www.meetup.com/DIYRobocars/events/237116510/
		
		
		TheJerf, HN dissident,go programmer
		http://www.jerf.org/iri/?page=4
		https://github.com/thejerf
		
		Crazy alt-right guy
		https://twitter.com/menaquinone4
		
		again
		https://twitter.com/Logo_Daedalus
		
		
		Old man take a look at my life, I'm a lot like you
		https://news.ycombinator.com/threads?id=losteverything
		
		f# "Tour" - good basis for starting
		https://docs.microsoft.com/en-us/dotnet/articles/fsharp/tour
		
		Taleb on Surgeons and the dog and the frisbee
		https://medium.com/incerto/surgeons-should-notlook-like-surgeons-23b0e2cf6d52#.q14omi99e
		
		
		2.27
		
		Joseph Campbell described believing in a literal, historical God as someone eating a menu believing that they were really eating the food. One clear component of the zombie meme is the spiritual starvation we are experiencing in the West. We are eating the menus so the speak- old, meaningless books written by foreign peoples from far off places thousands of years ago, and they give us no nourishment.
		
		DIYbio + CRISPR
		https://www.wsj.com/articles/diy-gene-editing-fast-cheapand-worrisome-1488164820
		
		
		I like Eco’s The Name of the Rose, but I love his Foucault’s Pendulum – I think of it as a life-changing book in my personal case,
		There’s a hackneyed phrase “transcend the genre”. I just reread The Player of Games and I can’t help feeling that it exists somehow on a completely different level of vividness, depth of character, beauty of style, imagination and convincing world-building than just about any other contemporary SF author I may quite like and appreciate (Stephenson, Stross, Vinge, Swawick…)
		
		
		WP on .NET
		http://www.peachpie.io/2017/02/wordpress-announcement.html
			
			discussion
			http://www.peachpie.io/benchmarks
			
			http://www.peachpie.io/benchmarks
			https://github.com/iolevel/peachpie
		
		
		Programmer Productivity from Redis Dev; great article
		http://antirez.com/news/112
		
			https://news.ycombinator.com/user?id=antirez
		
		
		https://en.wikipedia.org/wiki/Word_square
		
		
			https://github.com/jonbcard/scrabble-bot/blob/master/src/dictionary.txt
			
		Real time Text to Speech, from Baidu	http://research.baidu.com/deep-voice-production-quality-text-speech-system-constructed-entirely-deep-neural-networks/
		
		
		Developers! Developers!	https://channel9.msdn.com/events/Windows/Windows-Developer-Day-Creators-Update/Developer-tools-and-updates#time=17m30s
		
		
		UDP in browsers
		http://new.gafferongames.com/post/why_cant_i_send_udp_packets_from_a_browser/
		
		Irridium Satellite Communication - Recommended by phil g
		https://www.amazon.com/Eccentric-Orbits-Iridium-John-Bloom/dp/0802121683
		
		
		Robot Reinforcement learning
		https://www.technologyreview.com/s/603745/how-a-human-machine-mind-meld-could-make-robots-smarter/
		
		Goes against dang
		https://news.ycombinator.com/threads?id=lnanek2
		
		Profile of a Maker Luke Iseman in 2008
		http://austinpedicab.org/2008/10/06/austin-cronicle-interviews-luke-iseman/
		
		Whi invests in hardware, Bolt blog 2016
		https://blog.bolt.io/who-invests-in-hardware-2016-3b8149769924#.b1ksudzcg
		
		
		APL runtime environment
		http://www.dyalog.com/
		http://tryapl.org/w
		
		Historical Maps!
		http://www.archdaily.com/797814/71-thousand-high-res-historical-maps-available-for-free-download
		
		
		Geometry of the Universe
		https://www.quantamagazine.org/20170223-bootstrap-geometry-theory-space/
		
		GregBrockman
		https://blog.gregbrockman.com/my-path-to-openai

		RoboBartender
		http://vegas.eater.com/2017/3/6/14824690/first-robotic-bar-experience-in-the-world-to-las-vegas-strip
		
		Evan Sangaline, Poly-Programmer
		http://sangaline.com/
		
		
		Code review of Quake source code
		http://fabiensanglard.net/quake2/
		
		
	3.15
	
		"The six words “Do a huge volume of work” was the banner under which I marched."
		https://billmei.net/blog/silicon-valley-job-search
		
		
		Good example of unit testing
		http://marcin-chwedczuk.github.io/zen-and-the-art-of-unit-testing
		
			But...
			
			http://blog.cleancoder.com/uncle-bob/2017/03/03/TDD-Harms-Architecture.html
		
		
		
		Industry Dive - CI for various industries?
		http://www.industrydive.com/team/
		
		BeagelBone Blue - robotics computer
		https://beagleboard.org/blue
		
		
		Web scraping 
		http://sangaline.com/post/advanced-web-scraping-tutorial/
		
		c# to Java infographic
		http://www.harding.edu/fmccown/java_csharp_comparison.html#namespaces
		
		https://msdn.microsoft.com/en-us/library/sf0df423.aspx
		
		
		VR ball catching!
		https://www.disneyresearch.com/publication/catching-a-real-ball-in-virtual-reality/
		
		ML Journal
		http://distill.pub/about/
		
		
	Motion Tracking Dartboard	http://sploid.gizmodo.com/brilliant-motion-tracking-dart-board-guarantees-a-bulls-1793481286?utm_content=51211188&utm_medium=social&utm_source=twitter