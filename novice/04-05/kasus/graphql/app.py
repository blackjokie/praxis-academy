from flask import Flask
from graphene import ObjectType, String, Schema
from flask_graphql import GraphQLView

class Books(ObjectType):
    Title = String()
    Writer = String()
    Author = String()
    Year = String()
    def resolve_Title(self, args):
        return "Gang of Four"
    
    def resolve_Writer(self, args):
        return "Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides"
    
    def resolve_Author(self, args):
        return "Addison-Wesley"
    
    def resolve_Year(self, args):
        return "1994"

view_func = GraphQLView.as_view("graphql", schema=Schema(query=Books))

app = Flask(__name__)
app.add_url_rule("/graphql", view_func=view_func)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
