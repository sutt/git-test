
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
	
	Freeman Dyson, Scientist as rebel	https://books.google.com/books?id=Jhr8AwAAQBAJ&lpg=PT15&ots=MreY2f8eEg&dq=scientist%20as%20a%20rebel&pg=PT15#v=onepage&q&f=falsehttps://books.google.com/books?id=Jhr8AwAAQBAJ&lpg=PT15&ots=MreY2f8eEg&dq=scientist%20as%20a%20rebel&pg=PT15#v=onepage&q&f=false
	
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
   
   
   
   
   
   