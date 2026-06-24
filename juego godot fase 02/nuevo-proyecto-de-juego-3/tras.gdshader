shader_type canvas_item;

void fragment() {
    vec4 col = texture(TEXTURE, UV);
    // Si el color es muy cercano al blanco, hazlo invisible
    if (col.r > 0.95 && col.g > 0.95 && col.b > 0.95) {
        discard;
    }
    COLOR = col;
}