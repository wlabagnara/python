'''
  Created on 2020/04/19
  @author wlabagnara

  Model1 Class
'''


print("Model1 run as: {}".format(__name__))

# Model is not aware of View or Controller


class Model1:

    def __init__(self):
        self.counter = 0  # class properties

    def update_counter(self):
        self.counter += 1
        return self.counter


