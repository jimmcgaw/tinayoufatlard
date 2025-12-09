from django.http import JsonResponse, HttpRequest


def ask(request: HttpRequest) -> JsonResponse:
    question = request.GET.get("question", "")
    # Here you would integrate with your AI agent to get the answer
    answer = f"Simulated answer to: {question}"
    return JsonResponse({"answer": answer})