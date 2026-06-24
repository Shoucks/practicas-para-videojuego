extends Control

var madera = 50
var piedra = 40
var metal = 30

var recetas = {
	"Madera,Piedra": "Hacha",
	"Madera,Metal": "Martillo",
	"Metal,Piedra": "Pico"
}

var seleccionados = []
	
# Called when the node enters the scene tree for the first time.
func actualizar_materiales():
	$Panel/MaterialesTexto.text = "Madera: " + str(madera) + "\nPiedra: " + str(piedra) + "\nMetal: " + str(metal)

func _ready():
	actualizar_materiales()

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass

func actualizar_seleccion():
	$Panel/SeleccionLabel.text = "Seleccionados:\n"
	

	for material in seleccionados:
		$Panel/SeleccionLabel.text += material + "\n"

		

func comprobar_receta():
	if seleccionados.size() != 2:
		return
	seleccionados.sort()
	var clave = seleccionados[0] + "," + seleccionados[1]

	if recetas.has(clave):
		$Panel/ResultadoLabel.text = "Resultado: " + recetas[clave]
	else:
		$Panel/ResultadoLabel.text = "Resultado: Nada"

func _on_madera_button_pressed() -> void:
	if seleccionados.size() < 2:
		seleccionados.append("Madera")
		actualizar_seleccion()
		comprobar_receta()
		pass # Replace with function body.
	else:
		$Panel/SeleccionLabel.text = "Máximo 2 materiales"

func _on_piedra_button_pressed() -> void:
	if seleccionados.size() < 2:
		seleccionados.append("Piedra")
		actualizar_seleccion()
		comprobar_receta()
		pass # Replace with function body.
	else:
		$Panel/SeleccionLabel.text = "Máximo 2 materiales"
func _on_metal_button_pressed() -> void:
	if seleccionados.size() < 2:
		seleccionados.append("Metal")
		actualizar_seleccion()
		comprobar_receta()
		pass # Replace with function body.
	else:
		$Panel/SeleccionLabel.text = "Máximo 2 materiales"
