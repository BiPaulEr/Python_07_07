def psychologue():
    try:
        print("Hello")
        answer = yield
        yield None
        print(answer)
        if answer.endswith("?"):
            print("je tens pose des questions moi")
    except GeneratorExit as ge:
        print(f"{ge} ok")
    except Exception as e:
        print(f"{e} paye moi quand meme")

psycho = psychologue()
obj = next(psycho)
print(obj)
psycho.send("Ca va ?")
psycho.close()
psycho.throw(Exception("Exception"))
next(psycho)