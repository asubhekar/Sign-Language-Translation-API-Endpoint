# Sign Language Translation Endpoint API

This assignment is to focus on implementing backend API service for a simulated translation of sign language interpretation. This task can be done using Flask or Sanic web frameworks. I chose Sanic Web Framework as it is easier to debug. 

For this task, I have generated an HTML file which and an app.py file. 

### App.py file
asdasd
Functions: 
- async def index(request): This function renders the main HTML interface for the sign language translation tool. 
- async def translate(request): Processes the POST request which is a string input and returns the translated text in JSON format. It also handles exceptions and status codes.

    POST /translate
    
    Request:
    - Content-Type: application/json
    - Body: { "text": "string" }
    
    Response:
    - Success: { "message": "Translation successful", "translated_text": "Translated text: <input_text> (simulated)" }
    - Error: { "error": "string" }
    
    Status Codes:
    - 200: Successful translation
    - 400: Empty or missing text
    - 500: Internal server error
 
### index.html file
The HTML file creates a simple web page for sign language translation tool. It includes: 
- A simple form where the user can input text in English, which is submitted for translation.
- A script which handles the form submissions asynchrnously, sending the input text to the backend API and displaying the translated text or any error messages below the form.

<table>
  <tr>
    <td valign="top" width="50%">
      <img src = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMWUzaGVwaG96dmM5emF0eDRiNXNhZ2QxcGkwN2Fka2c1M25zeDQxdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/8qrrHSsrK9xpknGVNF/giphy.gif" align = "right"></img>
    </td>
    <td valign="top">
      <img src = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMWUzaGVwaG96dmM5emF0eDRiNXNhZ2QxcGkwN2Fka2c1M25zeDQxdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/8qrrHSsrK9xpknGVNF/giphy.gif" align = "right"></img>
    </td>
  </tr>
</table>
