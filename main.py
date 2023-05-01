from core.controller import Controller
from core.service import Service
from core.resource import Resource
from core.model import Model
from core.migration import Migration
from core.request import Request
from core.factory import Factory
from core.route import Route
from core.test import Test
from dotenv import load_dotenv
import os

load_dotenv()



project_path = os.getenv('APP_PATH')
model_name = input('Please input model name: ').title()
model_action = input('Please input action (1 - make, 0 - remove): ') == '1'

subjection = [
    Controller(name=model_name, project_path=project_path),
    Model(name=model_name, project_path=project_path),
    Service(name=model_name, project_path=project_path),

    Migration(name=model_name, project_path=project_path),
    Factory(name=model_name, project_path=project_path),

    Resource(name=model_name, project_path=project_path),
    Resource(name=model_name, project_path=project_path, template="DetailResource.stub"),

    Request(name=model_name, project_path=project_path),
    Request(name=model_name, project_path=project_path, class_name="UpdateRequest"),

    Test(name=model_name, project_path=project_path)
]

def helper(subjection, action: bool):
    return subjection.make() if action else subjection.remove()

for sub in subjection:
    print(sub.make() if model_action else sub.remove())


r = Route(name=model_name, project_path=project_path)

print(r.add() if model_action else r.remove())
