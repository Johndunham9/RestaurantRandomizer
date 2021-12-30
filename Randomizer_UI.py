from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from Radomizer import RestaurantStore, randomizer
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MainWindow(Screen):
    """The main window of the program"""
    pass


class AddRestaurantWindow(Screen):
    """Secondary Screen for adding restaurants"""

    def button_command(self):
        restaurants = RestaurantStore.instance()
        restaurants.add_restaurant(self.restaurant.text)
        print(restaurants.list)
        self.restaurant.text = ""


class RandomizeWindow(Screen):
    """Secondary Screen for randomizing restaurants from the list"""

    def random_restaurant_output(self):
        """Outputs one of two strings based on a condition """
        EMPTY = 0
        restaurants = RestaurantStore.instance()
        if len(restaurants.list) == EMPTY:
            return "You haven't added any restaurants"
        else:
            the_list = restaurants.list
            suggestion = randomizer(the_list)
            return f"How about {suggestion}?"

    def on_button_press(self):
        """This button command activates when the restaurant button in the randomize popup is pressed"""
        restaurant = RandomizeWindow.random_restaurant_output(self)
        layout = GridLayout(cols=1, padding=10)
        popupLabel = Label(text=restaurant)
        closeButton = Button(text="Close the pop-up")

        layout.add_widget(popupLabel)
        layout.add_widget(closeButton)

        # Instantiate the modal popup and display
        popup = Popup(title='Demo Popup',
                      content=layout)
        popup.open()

        # Attach close button press with popup.dismiss action
        closeButton.bind(on_press=popup.dismiss)


class RestaurantPopup(FloatLayout):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()

