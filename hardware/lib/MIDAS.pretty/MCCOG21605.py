import cadquery as cq

# Dimensions
glass_width = 54.58
glass_height = 20.80
glass_thickness = 1.10

num_pins = 8
pin_pitch = 1.27
pin_width = 0.4
pin_depth = 0.3 
pin_height = 10.0

# Calculate pin positions
total_pin_width = (num_pins - 1) * pin_pitch
start_x = -total_pin_width / 2

# Create glass body
glass = (cq.Workplane("XY")
    .workplane(offset=pin_height)
    .box(glass_width, glass_height, glass_thickness)
    .edges("|Z")
    .fillet(0.5))

# Create pins
pins = cq.Workplane("XY").workplane(offset=-pin_height)

for i in range(num_pins):
    pin_x = start_x + i * pin_pitch
    pin_y = - glass_height / 2
    
    pin = (cq.Workplane("XY")
        .workplane(offset=pin_height/2)
        .center(pin_x, pin_y)
        .box(pin_width, pin_depth, pin_height))
    
    pins = pins.union(pin)

# Combine and move glass to top
assembly = pins.union(glass.translate((0, 0, glass_thickness/2 - 3.0)))

# Export STEP file
assembly.val().exportStep("MCCOG21605.step")

print("STEP model generated: MCCOG21605.step")


