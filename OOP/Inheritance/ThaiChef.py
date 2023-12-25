from Chef import Chef

class ThaiChef(Chef):

    # Polymorphism: Override the make_special_dish method
    def make_special_dish(selfs):
        print("The chef makes egg fried rice")
    def make_tom_yum_kung(self):
        print("The chef makes Tom yum kung")
