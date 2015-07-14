
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
	
	
	
	
	
	
	
	
	
	