extends CharacterBody2D

var velocidad = 200

func _process(delta):

	var direccion = Vector2.ZERO

	if Input.is_key_pressed(KEY_W):
		direccion.y -= 1

	if Input.is_key_pressed(KEY_S):
		direccion.y += 1

	if Input.is_key_pressed(KEY_A):
		direccion.x -= 1

	if Input.is_key_pressed(KEY_D):
		direccion.x += 1

	position += direccion * velocidad * delta
