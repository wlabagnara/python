'''
  Created on 2020/04/19
  @author wlabagnara

  Controller1 Class

'''


# Controller is aware of Model and View...

from model1 import Model1 as Model
from view1 import View1 as View


print("Controller1 run as: {}".format(__name__))


class Controller1:

    def __init__(self):
        self.model = Model()    # binding instances
        self.view = View(self)  # pass controller instance to view

    def main(self):
        print('Controller1.main executed...')
        self.view.main()  # run View's main (will call infinite loop!)

    def on_button_click(self):
        result = self.model.update_counter()
        self.view.value_var.set(result)
        self.view.update_button()


if __name__ == '__main__':  # Main Program
    app = Controller1()
    app.main()

