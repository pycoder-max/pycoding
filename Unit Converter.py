from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class UnitConverterApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Input for the value to convert
        self.input_value = TextInput(hint_text='Enter value to convert', size_hint_y=None, height=50, multiline=False)
        self.layout.add_widget(self.input_value)
        
        # Spinner for conversion type selection
        self.conversion_type = Spinner(
            text='Select Conversion',
            values=('Meters to Kilometers', 'Grams to Kilograms', 'Celsius to Fahrenheit'),
            size_hint_y=None,
            height=50
        )
        self.layout.add_widget(self.conversion_type)
        
        # Button to trigger the conversion
        self.convert_button = Button(text="Convert", size_hint_y=None, height=50)
        self.convert_button.bind(on_press=self.convert)
        self.layout.add_widget(self.convert_button)
        
        # Label to show the conversion result
        self.result_label = Label(text="Result will be shown here", size_hint_y=None, height=50)
        self.layout.add_widget(self.result_label)
        
        return self.layout

    def convert(self, instance):
        try:
            value = float(self.input_value.text)  # Get the input value and convert it to a float
            
            if self.conversion_type.text == 'Meters to Kilometers':
                result = self.meters_to_kilometers(value)
                self.result_label.text = f"{value} meters is {result} kilometers"
            
            elif self.conversion_type.text == 'Grams to Kilograms':
                result = self.grams_to_kilograms(value)
                self.result_label.text = f"{value} grams is {result} kilograms"
                
            elif self.conversion_type.text == 'Celsius to Fahrenheit':
                result = self.celsius_to_fahrenheit(value)
                self.result_label.text = f"{value}°C is {result}°F"
                
            else:
                self.result_label.text = "Please select a conversion type"
                
        except ValueError:
            self.result_label.text = "Invalid input. Please enter a numeric value."
    
    # Conversion functions
    def meters_to_kilometers(self, meters):
        return meters / 1000
    
    def grams_to_kilograms(self, grams):
        return grams / 1000
    
    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

if __name__ == '__main__':
    UnitConverterApp().run()
