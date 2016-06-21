#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,Gdk,GObject #importamos la libreria

software_list = [("Firefox", 2015,  "C++"),
                 ("Eclipse", 2016, "Java" ),
                 ("Pitivi", 2024, "Python"),
                 ("Netbeans", 2000, "Java"),
                 ("Chrome", 1920, "C++"),
                 ("Filezilla", 2016, "C++"),
                 ("Bazaar", 2000, "Python"),
                 ("Git", 2010, "C"),
                 ("Linux Kernel", 2016, "C"),
                 ("GCC", 2015, "C"),
                 ("Frostwire", 2015, "Java")]


class GridWindow(Gtk.Window):    # Una Clase principal que herede Window
	
	

    def __init__(self):   # Constructor de la clase
        Gtk.Window.__init__(self, title="PyGObject") # Constructor de la clase padre
        self.set_border_width(60)

        grid = Gtk.Grid()
        self.add(grid)      
		
	
        self.button1 = Gtk.Button(label="StackSwitcher")
        self.button1.connect("clicked", self.on_button1_clicked)
        
        self.button2 = Gtk.Button(label="FlowBox")
        self.button2.connect("clicked",self.FlowBox)
        
        self.button3 = Gtk.Button(label="Notebook")
        self.button3.connect("clicked",self.notebook)
        
        self.button4 = Gtk.Button(label="ProgressBar")
        self.button4.connect("clicked",self.progresbar)
        
        self.button5 = Gtk.Button(label="Spinner")
        self.button5.connect("clicked",self.spinner)
        
        
        self.button6 = Gtk.Button(label="filtrado")
        self.button6.connect("clicked",self.filtrado)
        
        self.button7 = Gtk.Button(label="Entrada")
        self.button7.connect("clicked",self.entry)
        
        self.button8 = Gtk.Button(label="ComboBox")
        self.button8.connect("clicked",self.comboo)
        
        
        
        #gtk_grid_attach ( GtkGrid *grid ,GtkWidget *child ,gint left ,gint top ,gint width ,gint height )
        label = Gtk.Label ('     Ejemplos de PyGObject     ')
        grid.attach(label,0,0,4,1)
        label = Gtk.Label ('                               ')
        grid.attach(label,0,1,4,1)
        grid.attach_next_to(self.button1,label,Gtk.PositionType.BOTTOM,1,1)
        grid.attach(self.button2,1,2,1,1)
        grid.attach(self.button3,2,2,1,1)
        grid.attach(self.button4,3,2,1,1)
        label = Gtk.Label ('                               ')
        grid.attach(label,0,3,4,1)
        grid.attach_next_to(self.button5,label,Gtk.PositionType.BOTTOM,1,1)
        grid.attach(self.button6,1,4,1,1)
        grid.attach(self.button7,2,4,1,1)
        grid.attach(self.button8,3,4,1,1)
        
    def on_button1_clicked(self, widget):
		
		class StackWindow(Gtk.Window):
			def __init__(self):
				Gtk.Window.__init__(self, title="Stack Demo")
				self.set_border_width(10)
				vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
				self.add(vbox)
				stack = Gtk.Stack()
				stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
				stack.set_transition_duration(1000)
				checkbutton = Gtk.CheckButton("Click me!")
				stack.add_titled(checkbutton, "check", "Presiona el boton")
				label = Gtk.Label()
				label.set_markup("<big>You Only Live Once</big>")
				stack.add_titled(label, "Simulacion", "FRASE")
				stack_switcher = Gtk.StackSwitcher()
				stack_switcher.set_stack(stack)
				vbox.pack_start(stack_switcher, True, True, 0)
				vbox.pack_start(stack, True, True, 0)
		win = StackWindow()
		win.connect("delete-event", Gtk.main_quit)
		win.show_all()
		Gtk.main()		
        
    
    
    def FlowBox(self,widget):
		
		class FlowBoxWindow(Gtk.Window):

			def __init__(self):
				Gtk.Window.__init__(self, title="FlowBox Demo")
				self.set_border_width(10)
				self.set_default_size(300, 250)

				header = Gtk.HeaderBar(title="Flow Box")
				header.set_subtitle("Sample FlowBox app")
				header.props.show_close_button = True

				self.set_titlebar(header)

				scrolled = Gtk.ScrolledWindow()
				scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)

				flowbox = Gtk.FlowBox()
				flowbox.set_valign(Gtk.Align.START)
				flowbox.set_max_children_per_line(30)
				flowbox.set_selection_mode(Gtk.SelectionMode.NONE)

				self.create_flowbox(flowbox)

				scrolled.add(flowbox)

				self.add(scrolled)
				self.show_all()

			def color_swatch_new(self, str_color):
				color = Gdk.color_parse(str_color)

				rgba = Gdk.RGBA.from_color(color)
				button = Gtk.Button()

				area = Gtk.DrawingArea()
				area.set_size_request(24, 24)
				area.override_background_color(0, rgba)

				button.add(area)

				return button

			def create_flowbox(self, flowbox):
				colors = [
				'AliceBlue',
				'AntiqueWhite',
				'AntiqueWhite1',
				'AntiqueWhite2',
				'AntiqueWhite3',
				'AntiqueWhite4',
				'aqua',
				'aquamarine',
				'aquamarine1',
				'aquamarine2',
				'aquamarine3',
				'aquamarine4',
				'azure',
				'azure1',
				'azure2',
				'azure3',
				'azure4',
				'beige',
				'bisque',
				'bisque1',
				'bisque2',
				'bisque3',
				'bisque4',
				'black',
				'BlanchedAlmond',
				'blue',
				'blue1',
				'blue2',
				'blue3',
				'blue4',
				'BlueViolet',
				'brown',
				'brown1',
				'brown2',
				'brown3',
				'brown4',
				'burlywood',
				'burlywood1',
				'burlywood2',
				'burlywood3',
				'burlywood4',
				'CadetBlue',
				'CadetBlue1',
				'CadetBlue2',
				'CadetBlue3',
				'CadetBlue4',
				'chartreuse',
				'chartreuse1',
				'chartreuse2',
				'chartreuse3',
				'chartreuse4',
				'chocolate',
				'chocolate1',
				'chocolate2',
				'chocolate3',
				'chocolate4',
				'coral',
				'coral1',
				'coral2',
				'coral3',
				'coral4'
				]

				for color in colors:
					button = self.color_swatch_new(color)
					flowbox.add(button)


		win = FlowBoxWindow()
		win.connect("delete-event", Gtk.main_quit)
		win.show_all()
		Gtk.main()

	

    def notebook(self, widget):
		class MyWindow(Gtk.Window):
			def __init__(self):
				Gtk.Window.__init__(self, title="Simple Notebook Example")
				self.set_border_width(3)

				self.notebook = Gtk.Notebook()
				self.add(self.notebook)

				self.page1 = Gtk.Box()
				self.page1.set_border_width(10)
				self.page1.add(Gtk.Label("PyGObject es el «framework» de programación orientada\n a objetos que seusa en Gtk, todo viene porque Gtk está\n escrito en C y se creó esesistema para tener algo parecido\n a la programación orientada a objetos. Así que pyGObject\n serán los enlaces de python a este «framework». "))
				self.notebook.append_page(self.page1, Gtk.Label('Plain Title'))

				self.page2 = Gtk.Box()
				self.page2.set_border_width(10)
				self.page2.add(Gtk.Label('Pagina con imagen en el titulo'))
				
				self.notebook.append_page(
					self.page2,
					Gtk.Image.new_from_icon_name(
						"help-about",
						Gtk.IconSize.MENU
					)
				)

		win = MyWindow()
		win.connect("delete-event", Gtk.main_quit)
		win.show_all()
		Gtk.main()
		
	
    def progresbar(self, widget):
        class ProgressBarWindow(Gtk.Window):
		
			def __init__(self):
				
				Gtk.Window.__init__(self, title="Barra progresiva")
				self.set_border_width(70)

				vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
				self.add(vbox)

				self.progressbar = Gtk.ProgressBar()
				vbox.pack_start(self.progressbar, True, True, 0)

				button = Gtk.CheckButton("Mostrar Texto")
				button.connect("toggled", self.on_show_text_toggled)
				vbox.pack_start(button, True, True, 0)

				button = Gtk.CheckButton("Modo de Actividad")
				button.connect("toggled", self.on_activity_mode_toggled)
				vbox.pack_start(button, True, True, 0)

				button = Gtk.CheckButton("Derecha a Izquierda")
				button.connect("toggled", self.on_right_to_left_toggled)
				vbox.pack_start(button, True, True, 0)

				self.timeout_id = GObject.timeout_add(100, self.on_timeout, None)
				self.activity_mode = False

			def on_show_text_toggled(self, button):
				show_text = button.get_active()
				if show_text:
					text = "Cargando..."
				else:
					text = None
				self.progressbar.set_text(text)
				self.progressbar.set_show_text(show_text)

			def on_activity_mode_toggled(self, button):
				self.activity_mode = button.get_active()
				if self.activity_mode:
					self.progressbar.pulse()
				else:
					self.progressbar.set_fraction(0.0)

			def on_right_to_left_toggled(self, button):
				value = button.get_active()
				self.progressbar.set_inverted(value)

			def on_timeout(self, user_data):
				"""
				Update value on the progress bar
				"""
				if self.activity_mode:
					self.progressbar.pulse()
				else:
					new_value = self.progressbar.get_fraction() + 0.01

					if new_value > 1:
						new_value = 0

					self.progressbar.set_fraction(new_value)

				# As this is a timeout function, return True so that it
				# continues to get called
				return True
		
		
	win = ProgressBarWindow()
	win.connect("delete-event", Gtk.main_quit)
	win.show_all()
	Gtk.main()

		
    def spinner(self, widget):
		class SpinnerAnimation(Gtk.Window):

			def __init__(self):

				Gtk.Window.__init__(self, title="Spinner")
				self.set_border_width(3)
				self.connect("delete-event", Gtk.main_quit)

				self.button = Gtk.ToggleButton("Iniciar Spinning") # button inicial 
				self.button.connect("toggled", self.on_button_toggled)
				self.button.set_active(False)

				self.spinner = Gtk.Spinner()

				self.table = Gtk.Table(3, 2, True)
				self.table.attach(self.button, 0, 2, 0, 1)
				self.table.attach(self.spinner, 0, 2, 2, 3)

				self.add(self.table)
				self.show_all()

			def on_button_toggled(self, button):

				if button.get_active():
					self.spinner.start()
					self.button.set_label("Detener Spinning")

				else:
					self.spinner.stop()
					self.button.set_label("Iniciar Spinning")
		myspinner = SpinnerAnimation()
		Gtk.main()


   
    def filtrado(self, widget):
		class TreeViewFilterWindow(Gtk.Window):

			def __init__(self):
				Gtk.Window.__init__(self, title="Treeview Filter Demo")
				self.set_border_width(10)

			

				#Configurar la self.grid las posiciones de los elementos
				self.grid = Gtk.Grid()
				self.grid.set_column_homogeneous(True)
				self.grid.set_row_homogeneous(True)
				self.add(self.grid)

				#Creación del modelo de ListStore
				self.software_liststore = Gtk.ListStore(str, int, str)
				for software_ref in software_list:
					self.software_liststore.append(list(software_ref))
				self.current_filter_language = None

				#Creando el filtro, empleando el modelo liststore
				self.language_filter = self.software_liststore.filter_new()
				
				self.language_filter.set_visible_func(self.language_filter_func)

				#creating the treeview, making it use the filter as a model, and adding the columns
				self.treeview = Gtk.TreeView.new_with_model(self.language_filter)
				for i, column_title in enumerate(["Software", "Release Year", "Programming Language"]):
					renderer = Gtk.CellRendererText()
					column = Gtk.TreeViewColumn(column_title, renderer, text=i)
					self.treeview.append_column(column)

				#creating buttons to filter by programming language, and setting up their events
				self.buttons = list()
				for prog_language in ["Java", "C", "C++", "Python", "Todos"]:
					button = Gtk.Button(prog_language)
					self.buttons.append(button)
					button.connect("clicked", self.on_selection_button_clicked)

				#setting up the layout, putting the treeview in a scrollwindow, and the buttons in a row
				self.scrollable_treelist = Gtk.ScrolledWindow()
				self.scrollable_treelist.set_vexpand(True)
				self.grid.attach(self.scrollable_treelist, 0, 0, 8, 10)
				self.grid.attach_next_to(self.buttons[0], self.scrollable_treelist, Gtk.PositionType.BOTTOM, 1, 1)
				for i, button in enumerate(self.buttons[1:]):
					self.grid.attach_next_to(button, self.buttons[i], Gtk.PositionType.RIGHT, 1, 1)
				self.scrollable_treelist.add(self.treeview)

				self.show_all()

			def language_filter_func(self, model, iter, data):
				"""Tests if the language in the row is the one in the filter"""
				if self.current_filter_language is None or self.current_filter_language == "Todos":
					return True
				else:
					return model[iter][2] == self.current_filter_language

			def on_selection_button_clicked(self, widget):
				"""Called on any of the button clicks"""
				#we set the current language filter to the button's label
				self.current_filter_language = widget.get_label()
				print("%s language selected!" % self.current_filter_language)
				#we update the filter, which updates in turn the view
				self.language_filter.refilter()


		win = TreeViewFilterWindow()
		win.connect("delete-event", Gtk.main_quit)
		win.show_all()
		Gtk.main()
        


    def entry(self, widget):
		class EntryWindow(Gtk.Window):
			def __init__(self):
				Gtk.Window.__init__(self, title="Entradas")
				self.set_size_request(200, 100)

				self.timeout_id = None

				vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
				self.add(vbox)

				self.entry = Gtk.Entry()
				self.entry.set_text("ESTOY DEFENDIENDO")
				vbox.pack_start(self.entry, True, True, 0)

				hbox = Gtk.Box(spacing=6)
				vbox.pack_start(hbox, True, True, 0)
				
				self.check_editable = Gtk.CheckButton("Editable")
				self.check_editable.connect("toggled", self.on_editable_toggled)
				self.check_editable.set_active(True)
				hbox.pack_start(self.check_editable, True, True, 0)

				self.check_visible = Gtk.CheckButton("Visible")
				self.check_visible.connect("toggled", self.on_visible_toggled)
				self.check_visible.set_active(True)
				hbox.pack_start(self.check_visible, True, True, 0)

				self.pulse = Gtk.CheckButton("Pulse")
				self.pulse.connect("toggled", self.on_pulse_toggled)
				self.pulse.set_active(False)
				hbox.pack_start(self.pulse, True, True, 0)

				self.icon = Gtk.CheckButton("Icon")
				self.icon.connect("toggled", self.on_icon_toggled)
				self.icon.set_active(False)
				hbox.pack_start(self.icon, True, True, 0)

			def on_editable_toggled(self, button):
				value = button.get_active()
				self.entry.set_editable(value)

			def on_visible_toggled(self, button):
				value = button.get_active()
				self.entry.set_visibility(value)

			def on_pulse_toggled(self, button):
				if button.get_active():
					self.entry.set_progress_pulse_step(0.2)
					# Call self.do_pulse every 100 ms
					self.timeout_id = GObject.timeout_add(100, self.do_pulse, None)
				else:
					# Don't call self.do_pulse anymore
					GObject.source_remove(self.timeout_id)
					self.timeout_id = None
					self.entry.set_progress_pulse_step(0)

			def do_pulse(self, user_data):
				self.entry.progress_pulse()
				return True

			def on_icon_toggled(self, button):
				if button.get_active():
					icon_name = "system-search-symbolic"
				else:
					icon_name = None
				self.entry.set_icon_from_icon_name(Gtk.EntryIconPosition.PRIMARY,
					icon_name)
		win = EntryWindow()
		win.connect("delete-event", Gtk.main_quit)
		win.show_all()
		Gtk.main()
        
 

    def comboo(self, widget):
		class ComboBoxWindow(Gtk.Window):
			def __init__(self):
				Gtk.Window.__init__(self, title="ComboBox ")

				self.set_border_width(10)

				name_store = Gtk.ListStore(int, str)
				name_store.append([1, "UES-FMO"])
				name_store.append([11, "DOn Bosco"])
				name_store.append([12, "UCA"])
				name_store.append([2, "Evangelica"])
				name_store.append([3, "UMA"])
				name_store.append([31, "ITCA-FEPADE"])

				vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

				name_combo = Gtk.ComboBox.new_with_model_and_entry(name_store)
				name_combo.connect("changed", self.on_name_combo_changed)
				name_combo.set_entry_text_column(1)
				vbox.pack_start(name_combo, False, False, 0)

				country_store = Gtk.ListStore(str)
				countries = ["EL Salvador", "Guatemala", "Honduras", "Nicaragua", "Costa Rica",
					"Estados Unidos","Uruguay"]
				for country in countries:
					country_store.append([country])

				country_combo = Gtk.ComboBox.new_with_model(country_store)
				country_combo.connect("changed", self.on_country_combo_changed)
				renderer_text = Gtk.CellRendererText()
				country_combo.pack_start(renderer_text, True)
				country_combo.add_attribute(renderer_text, "text", 0)
				vbox.pack_start(country_combo, False, False, True)

				currencies = ["Euro", "US Dollars", "British Pound", "Japanese Yen",
					"Russian Ruble", "Mexican peso", "Swiss franc"]
				currency_combo = Gtk.ComboBoxText()
				currency_combo.set_entry_text_column(0)
				currency_combo.connect("changed", self.on_currency_combo_changed)
				for currency in currencies:
					currency_combo.append_text(currency)

				vbox.pack_start(currency_combo, False, False, 0)

				self.add(vbox)

			def on_name_combo_changed(self, combo):
				tree_iter = combo.get_active_iter()
				if tree_iter != None:
					model = combo.get_model()
					row_id, name = model[tree_iter][:2]
					print("Seleccionado: ID=%d, Universidad: %s" % (row_id, name))
				else:
					entry = combo.get_child()
					print("Entered: %s" % entry.get_text())

			def on_country_combo_changed(self, combo):
				tree_iter = combo.get_active_iter()
				if tree_iter != None:
					model = combo.get_model()
					country = model[tree_iter][0]
					print("Selected: Pais: %s" % country)

			def on_currency_combo_changed(self, combo):
				text = combo.get_active_text()
				if text != None:
					print("Selected: moneda=%s" % text)
					
		win = ComboBoxWindow()
		win.connect("delete-event", Gtk.main_quit)
		win.show_all()
		Gtk.main() 
		

		
win = GridWindow() #creamos una ventana
win.connect("delete-event", Gtk.main_quit)#le conectamos un evento a la ventana
win.show_all() #mostramos la ventana
Gtk.main() # ejecutamos la aplicacion con un main

