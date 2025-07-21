
<div>
    <h1>Assignment 4</h1>
    <hr>
    <i style = "font-size: 19px;">This assignment is about implementing the Leader Election Problem</i>
</div>


<div>
    <h2>Usage</h2>
    <ol style = "font-size: 19px;">
        <li>Run the ring component file: “myleprocess.py” with python interpreter, <b>pass the config file as command line argument</b></li>  
        <li>Run as many instances: “myleprocess.py.py” as necessary with 
            python interpreter</li>
        <li>Start the instances as any order you like</li>
        <li>The instances will terminate when a leader is decided, with the leader's ID printed on the screen</li>
    </ol>
    <ul style = "font-size: 19px;">
        <li>&starf;<b>If no command line argument is provided, then the process will use the default path "<i>./a4/config.txt</i>"</b>&starf;</li>
        <li>&starf;<b>The log file will be generated after termination</b>&starf;</li>
    </ul>
</div>

<div>
    <hr>
    <h2>Example Run</h2>
    <h3>Client1</h3>
    <pre style="font-size: 19px;"> 
C:\Python313\python.exe "C:\Users\grape\OneDrive - sjsu.edu\Su_25_CS158A_CpuNetwork\cs158a\a3\myleprocess.py" a3/config.txt 
Sent: uuid=ceb8f74d-3977-4a88-bfab-1fc80689666e, flag=0
no config file provided, default to 'a4/config.txt'
Sent: uuid=29da52a9-6d42-4151-99e9-7aa198b91020, flag=0
Sent: uuid=3b2b3268-f7be-4388-9baf-da35be1325e5, flag=0
Received: uuid=3b2b3268-f7be-4388-9baf-da35be1325e5, flag=0, greater, 0, forwarded
Sent: uuid=8c06130a-6b84-4fc4-9276-d75ad9dda295, flag=0
Received: uuid=8c06130a-6b84-4fc4-9276-d75ad9dda295, flag=0, greater, 0, forwarded
Leader is decided to 8c06130a-6b84-4fc4-9276-d75ad9dda295.
Sent: uuid=8c06130a-6b84-4fc4-9276-d75ad9dda295, flag=1
    </pre>
    <h3>Client 2</h3>
    <pre style="font-size: 19px;"> 
Sent: uuid=8c06130a-6b84-4fc4-9276-d75ad9dda295, flag=0
Sent: uuid=8c06130a-6b84-4fc4-9276-d75ad9dda295, flag=0
Received: uuid=29da52a9-6d42-4151-99e9-7aa198b91020, flag=0, less, 0, ignored
Sent: uuid=8c06130a-6b84-4fc4-9276-d75ad9dda295, flag=0
Received: uuid=3b2b3268-f7be-4388-9baf-da35be1325e5, flag=0, less, 0, ignored
Sent: uuid=8c06130a-6b84-4fc4-9276-d75ad9dda295, flag=1
Leader is decided to 8c06130a-6b84-4fc4-9276-d75ad9dda295.
    </pre>
    <h3>Client 3</h3>
    <pre style="font-size: 19px;"> 
Sent: uuid=8c06130a-6b84-4fc4-9276-d75ad9dda295, flag=0
Received: uuid=8c06130a-6b84-4fc4-9276-d75ad9dda295, flag=0, greater, 0, forwarded
Sent: uuid=3b2b3268-f7be-4388-9baf-da35be1325e5, flag=0
Sent: uuid=8c06130a-6b84-4fc4-9276-d75ad9dda295, flag=0
Received: uuid=8c06130a-6b84-4fc4-9276-d75ad9dda295, flag=0, greater, 0, forwarded
Leader is decided to 8c06130a-6b84-4fc4-9276-d75ad9dda295.
Sent: uuid=8c06130a-6b84-4fc4-9276-d75ad9dda295, flag=1
    </pre>
</div>
