from PIL import Image, ImageDraw

# Создаем окно
width = 400
height = 400
background_color = (120,219,226)  # Голубой
image = Image.new("RGB", (width, height), background_color)

draw = ImageDraw.Draw(image)

# Трава
grass_color = (0, 128, 0)  # Темно зеленая трава
grass_top = 3 * height // 4
grass_bottom = height
draw.rectangle((0, grass_top, width, grass_bottom), fill=grass_color)

# Стена
wall_color = (164,116,73)  # Деревянный
wall_left = width // 4
wall_top = height // 2
wall_right = 3 * width // 4
wall_bottom = 3 * height // 4
draw.rectangle((wall_left, wall_top, wall_right, wall_bottom), fill=wall_color)

# Дверь
door_color = (78,53,36)
door_left = wall_left + (wall_right - wall_left) * 0.5
door_top = height * 0.6
door_right = door_left + width * 0.1
door_bottom = wall_bottom
draw.rectangle((door_left, door_top, door_right, door_bottom), fill=door_color)

# Крыша
roof_color = (166,47,32)  # Черепица
roof_top = (width // 2, height // 4)
roof_left = (width // 4, height // 2)
roof_right = (3 * width // 4, height // 2)
roof_points = [roof_top, roof_left, roof_right]
draw.polygon(roof_points, fill=roof_color)

# Солнце
sun_color = (255, 255, 0)  # Желтый
sun_radius = 50
sun_center = (width - sun_radius - 10, sun_radius + 10)
draw.ellipse((sun_center[0] - sun_radius, sun_center[1] -
              sun_radius, sun_center[0] + sun_radius, sun_center[1] + sun_radius), fill=sun_color)

# Save the image with the drawn house
image.save("house.png")

# Display the image
image.show()
