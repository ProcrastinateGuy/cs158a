<div>
    <h1>Assignment 1: </h1>
    <hr>
    <h3>contact: <u>shih-ru,sheng@sjsu.edu</u></h3>
    <p>This assignment is about creating a simple client-server
    program, with variable length
    </p>
    <hr>
    <h2>Variable-length message</h2>
    <ul>
        <li>The client and server can handle an arbitrary length of messages.</li>
        <li>The message in this version has a number 
            before the message text to tell the number of characters in the 
            text.(first 2 digits)</li>
        <li>The server program will keep handling the text until it sees the end of the message based on the specified length.</li>
    </ul>
    <h2>Message Format</h2>
    <ul>
        <li>The first 2 characters of a message is the length of the message</li>
        <li>All characters are between UTF8 U+0000 and U+007F.</li>
    </ul>
    <h2>Usage</h2>
    <ol>
        <li>Start the myvlenserver.py</li>
        <li>After seeing <code>"server is listening"</code>, Start the myvlenclient.py</li>
        <li>&starf;<b>You must start the server before starting the client</b>&starf;</li>
    </ol>
    <hr>
    <div>
        <h2>Example Output</h2>
        <h3>Server Side:</h3>
        <blockquote>
            C:\Python313\python.exe ".\cs158a\a1\myvlserver.py"<br>
            server is listening<br>
            Connection established with 127.0.0.1 at port 60299<br>
            Number of transaction: 2<br>
            client specified length: 99<br>
            client message actual length: 99<br>
        </blockquote>
        <br>
        <h3>Client Side:</h3>
        <blockquote>
            C:\Python313\python.exe ".\cs158a\a1\myvlclient.py" <br>
            Input lowercase sentence:<br>99asdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdaqweqweqweqweqweqweqweqweqweqweqweqw<br>
            status: OK<br>
            chunk# 0, length: 64, msg: ASDASDASDASDASDASDASDASDASDASDASDASDASDASDASDASDASDASDASDASDASDA<br>
            chunk# 1, length: 35, msg: QWEQWEQWEQWEQWEQWEQWEQWEQWEQWEQWEQW<br>
            <br>
            Process finished with exit code 0<br>
        </blockquote>
    </div>

</div>
