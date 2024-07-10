from sanic import Sanic, response
from sanic.request import Request
from sanic.response import HTTPResponse, json
from sanic.exceptions import SanicException

app = Sanic("SignLanguageTranslationAPI")

@app.route("/")
async def index(request):
    return await response.file("static/index.html")

@app.route("/translate", methods=["POST"])
async def translate(request: Request) -> HTTPResponse:
    try:
        data = request.json
        text = data.get("text", "").strip()

        if not text:
            raise SanicException("No text provided", status_code=400)

        # Simulate translation process
        translated_text = f"Successful translation of simulated text : {text}"
        

        return json({"message": "Status code 200", "translated_text": translated_text})
        
    except SanicException as e:
        return json({"error": e.args[0]}, status=e.status_code)
        
    except Exception as e:
        return json({"error": "An unexpected error occurred"}, status=500)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
