import Wpf

from System.Windows import Application, Window, MessageBox
class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'WpfApplication2.xaml')
    

    def button_Click(self, sender, event):
        x= self.textboxNama.Text.ToString()

        if x == "" or self.comboBox1.Text == None or (self.Makan.IsChecked == False and self.Tidur.IsChecked == False and self.Jalan.IsChecked == False) :
            MessageBox.Show("Belum Diisi")

        else:
        #menentukan Gender
            if self.comboBox1.Text == self.comboBox1.Items.GetItemAt(0).ToString():
                gender = "Mas"
               # MessageBox.Show("Halo Mas "+x+ " yang suka")
            
            elif self.comboBox1.Text == self.comboBox1.Items.GetItemAt(1).ToString():
                gender = "mbak"
               # MessageBox.Show("Halo Mbak ")
        
            #menentukan Hobi
            if self.Makan.IsChecked:
                    hobi="Makan"
            elif self.Tidur.IsChecked:
                hobi="Tidur"
            elif self.Jalan.IsChecked:
                hobi="Jalan-Jalan"
            MessageBox.Show("Halo "+gender+" "+x+" yang hobinya "+hobi)
        pass
        pass
if __name__ == '__main__':
    Application().Run(MyWindow())
    