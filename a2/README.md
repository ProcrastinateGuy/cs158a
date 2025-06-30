
<div>
    <h1>Assignment 2</h1>
    <hr>
    <i style = "font-size: 19px;">This assignment is about creating a synchronous chat service for multiple users</i>
</div>


<div>
    <h2>Usage</h2>
    <ol style = "font-size: 19px;">
        <li>Run the server file: “mychatserver.py” with python interpreter</li>  
        <li>Run as many client file instances: “mychatclient.py” as necessary with 
            python interpreter</li>
        <li>In the client instance, type the message you want to send, other people's
            messages will show on the terminal</li>
        <li>To exit the chat, type exit in the client instance, this will disconnect you from the server</li>
    </ol>
    <ul style = "font-size: 19px;">
        <li>&starf;<b>You must start the server before starting the client</b>&starf;</li>
        <li>&starf;<b>You can check the complete chat history from the server</b>&starf;</li>
    </ul>
</div>

<div>
    <hr>
    <h2>Example Run</h2>
    <h3>Server</h3>
    <pre style="font-size: 19px;"> 
        server listen at 127.0.0.1:15000<br>
        New connection from ('127.0.0.1', 55743)<br>
        New connection from ('127.0.0.1', 55745)<br>
        55745: hELLO<br>
        55745: OOPS UPPERCASE<br>
        55745: ha<br>
        55743: hey<br>
        55743: don't forget to submit the homework!<br>
        55745: alrighty<br>
        55745: gtg<br>
        55743: cya 55745<br>
        55745: cya 55743<br>
    </pre>
    <h3>Client 1</h3>
    <pre style="font-size: 19px;"> 
        connected to server, type 'exit' to quit<br>
        Your name is: 55745<br>
        ---------------------------------------------<br>
        hELLO<br>
        OOPS UPPERCASE<br>
        ha<br>
        55743: hey<br>
        55743: don't forget to submit the homework!<br>
        alrighty<br>
        gtg<br>
        55743: cya 55745<br>
        cya 55743<br>
        exit<br>
        Disconnected from server<br>
        Process finished with exit code 0<br>
    </pre>
    <h3>Client 2</h3>
    <pre style="font-size: 19px;"> 
        connected to server, type 'exit' to quit<br>
        Your name is: 55743<br>
        ---------------------------------------------<br>
        55745: hELLO<br>
        55745: OOPS UPPERCASE<br>
        55745: ha<br>
        hey<br>
        don't forget to submit the homework!<br>
        55745: alrighty<br>
        55745: gtg<br>
        cya 55745<br>
        55745: cya 55743<br>
        exit<br>
        Disconnected from server<br>
        Process finished with exit code 0<br>
    </pre>
</div>
