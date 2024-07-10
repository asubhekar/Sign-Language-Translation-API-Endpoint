# Sign Language Translation Endpoint API

This assignment is to focus on implementing backend API service for a simulated translation of sign language interpretation. This task can be done using Flask or Sanic web frameworks. I chose Sanic Web Framework as it is easier to debug. The error codes were tested using Postman.

For this task, I have generated an HTML file which and an app.py file. 

### App.py file

Functions: 
- async def index(request): This function renders the main HTML interface for the sign language translation tool. 
- async def translate(request): Processes the POST request which is a string input and returns the translated text in JSON format. It also handles exceptions and status codes.

    POST /translate
    
    Request:
    - Content-Type: application/json
    - Body: { "text": "string" }
    
    Response:
    - Success: { "message": "Translation successful", "translated_text": "Successful translation of simulated text {input_text}" }
    - Error: { "error": "Error: No Text Provided" }
    
    Status Codes:
    - 200: Successful translation
    - 400: Empty or missing text (exception caught using SanicException)
    - 500: Internal server error (exception caught using Exception)
 
### index.html file
The HTML file creates a simple web page for sign language translation tool. It includes: 
- A simple form where the user can input text in English, which is submitted for translation.
- A script which handles the form submissions asynchrnously, sending the input text to the backend API and displaying the translated text or any error messages below the form.

<table>
  <tr>
    <td valign="top" width="50%">
      <img src = "https://github.com/asubhekar/Sign-Language-Translation-Endpoint-API/blob/main/images/Screenshot%202024-07-10%20at%204.15.34%E2%80%AFPM.png" align = "right"></img>
    </td>
    <td valign="top">
      <img src = "https://github.com/asubhekar/Sign-Language-Translation-Endpoint-API/blob/main/images/Screenshot%202024-07-10%20at%204.15.45%E2%80%AFPM.png" align = "right"></img>
    </td>
  </tr>
</table>
