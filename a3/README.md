
<div>
    <h1>Assignment 3</h1>
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
        <li>&starf;<b>You must pass the config file as the command line argument</b>&starf;</li>
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
Sent: uuid=ceb8f74d-3977-4a88-bfab-1fc80689666e, flag=0
Received: uuid=c0f3fbe8-25b0-40dc-b5e1-0ae2f4e4a15e, flag=0, less, 0, ignored
Sent: uuid=ed2d805c-d3a1-401c-a461-1bf4fb26e7fe, flag=0
Received: uuid=ed2d805c-d3a1-401c-a461-1bf4fb26e7fe, flag=0, greater, 0, forwarded
Leader is decided to ed2d805c-d3a1-401c-a461-1bf4fb26e7fe.
Sent: uuid=ed2d805c-d3a1-401c-a461-1bf4fb26e7fe, flag=1
Received: uuid=ed2d805c-d3a1-401c-a461-1bf4fb26e7fe, flag=1, greater, 0, forwarded
    </pre>
    <h3>Client 2</h3>
    <pre style="font-size: 19px;"> 
C:\Python313\python.exe "C:\Users\grape\OneDrive - sjsu.edu\Su_25_CS158A_CpuNetwork\cs158a\a3\myleprocess.py" a3/configb.txt 
Sent: uuid=ed2d805c-d3a1-401c-a461-1bf4fb26e7fe, flag=0
Sent: uuid=ed2d805c-d3a1-401c-a461-1bf4fb26e7fe, flag=0
Received: uuid=ceb8f74d-3977-4a88-bfab-1fc80689666e, flag=0, less, 0, ignored
Sent: uuid=ed2d805c-d3a1-401c-a461-1bf4fb26e7fe, flag=0
Received: uuid=ceb8f74d-3977-4a88-bfab-1fc80689666e, flag=0, less, 0, ignored
Sent: uuid=ed2d805c-d3a1-401c-a461-1bf4fb26e7fe, flag=1
Leader is decided to ed2d805c-d3a1-401c-a461-1bf4fb26e7fe.
Sent: uuid=ed2d805c-d3a1-401c-a461-1bf4fb26e7fe, flag=1
    </pre>
    <h3>Client 3</h3>
    <pre style="font-size: 19px;"> 
C:\Python313\python.exe "C:\Users\grape\OneDrive - sjsu.edu\Su_25_CS158A_CpuNetwork\cs158a\a3\myleprocess.py" a3/configc.txt 
Sent: uuid=ed2d805c-d3a1-401c-a461-1bf4fb26e7fe, flag=0
Sent: uuid=c0f3fbe8-25b0-40dc-b5e1-0ae2f4e4a15e, flag=0
Received: uuid=ed2d805c-d3a1-401c-a461-1bf4fb26e7fe, flag=0, greater, 0, forwarded
Sent: uuid=ed2d805c-d3a1-401c-a461-1bf4fb26e7fe, flag=0
Received: uuid=ed2d805c-d3a1-401c-a461-1bf4fb26e7fe, flag=0, greater, 0, forwarded
Leader is decided to ed2d805c-d3a1-401c-a461-1bf4fb26e7fe.
Sent: uuid=ed2d805c-d3a1-401c-a461-1bf4fb26e7fe, flag=1
Received: uuid=ed2d805c-d3a1-401c-a461-1bf4fb26e7fe, flag=1, greater, 0, forwarded
    </pre>
</div>
