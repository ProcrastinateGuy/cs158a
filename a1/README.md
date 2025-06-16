<div>
    <h1>Assignment 1: </h1>
    <hr>
    <p>This assignment is about creating a simple client-server
    program, with variable length
    </p>
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
        <li>First 2 bytes of a message is the length of the message</li>
        <li>All characters are between UTF8 U+0000 and U+007F.</li>
    </ul>
</div>
