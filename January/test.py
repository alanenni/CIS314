from PIL import Image, ImageDraw

# Create a new image with a white background
width, height = 400, 200
image = Image.new('RGB', (width, height), color='white')

# Create a drawing object
draw = ImageDraw.Draw(image)

# Draw the car body (red rectangle)
draw.rectangle([50, 100, 350, 180], fill='red', outline='black')

# Draw the roof
draw.polygon([(100, 100), (200, 60), (300, 100)], fill='red', outline='black')

# Draw wheels
draw.ellipse([75, 150, 125, 200], fill='black')
draw.ellipse([275, 150, 325, 200], fill='black')

# Save the image
image.save('ferrari_2d.png')
