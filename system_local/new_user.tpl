<style>
form {
        /* Center the form on the page */
        margin: 0 auto;
        width: 400px;
        /* Form outline */
        padding: 1em;
        border: 1px solid #CCC;
        border-radius: 1em;
    }
    
    ul {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    
    form li + li {
        margin-top: 1em;
    }
    
    label {
        /* Uniform size & alignment */
        display: inline-block;
        width: 90px;
        text-align: right;
    }
    
    input, 
    textarea {
        /* To make sure that all text fields have the same font settings
        By default, textareas have a monospace font */
        font: 1em sans-serif;
    
        /* Uniform text field size */
        width: 300px;
        box-sizing: border-box;
    
        /* Match form field borders */
        border: 1px solid #999;
    }
    
    input:focus, 
    textarea:focus {
        /* Additional highlight for focused elements */
        border-color: #000;
    }
    
    textarea {
        /* Align multiline text fields with their labels */
        vertical-align: top;
    
        /* Provide space to type some text */
        height: 5em;
    }
    
    .button {
        /* Align buttons with the text fields */
        padding-left: 90px; /* same size as the label elements */
    }
    
    button {
        /* This extra margin represent roughly the same space as the space
        between the labels and their text fields */
        margin-left: .5em;
    }
    </style>

    <h2><center>New User</center></h2>
    <form action="/new_user" method='POST'> 
        <ul>
            <li>
                <label for="f_name">Name:</label>
                <input type="text" name="f_name" />
            </li>
             <li>
                <label for="myemail">E-mail:</label>
                <input type="text" name="myemail" />
            </li>
            <li>
                <label for="msg">Message:</label>
                <textarea name="msg"></textarea>
            </li>
            <li>
                <input type="submit" name="save" value="Send your message">
            </li>
        </ul>
    </form>

<!---
<p>New Task</p>
<form action="/new_item" method='POST'>
    <input type="text" size="100" maxlength="100" name="new_item">
    <input type="submit" name="save" value="Save">
</form> ----> 