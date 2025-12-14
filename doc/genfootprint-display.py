"""
KiCad Footprint and STEP Model Generator for LCD Display
Glass: 54.58 x 20.80 mm
8 pins, 1.27mm pitch, centered on bottom
Pin height: 12mm, Glass thickness: 1.10mm
"""

def generate_kicad_footprint():
    """Generate KiCad footprint file (.kicad_mod)"""
    
    # Display dimensions
    glass_width = 54.58
    glass_height = 20.80
    glass_thickness = 1.10
    
    # Pin specifications
    num_pins = 8
    pin_pitch = 1.27
    pin_names = ["VOUT", "CAP1N", "CAP2N", "VDD", "VSS", "SDA", "SCL", "RST"]
    
    # Calculate pin positions (centered on bottom)
    total_pin_width = (num_pins - 1) * pin_pitch
    start_x = -total_pin_width / 2
    
    # Pad dimensions (standard for 1.27mm pitch)
    pad_width = 0.6
    pad_height = 1.5
    
    footprint = f'''(footprint "LCD_54.58x20.80_8Pin_1.27mm"
  (version 20240108)
  (generator "pcbnew")
  (generator_version "8.0")
  (layer "F.Cu")
  (descr "LCD Display 54.58x20.80mm, 8 pins, 1.27mm pitch")
  (tags "LCD display")
  
  (attr smd)
  
  (fp_text reference "REF**" (at 0 {-glass_height/2 - 2}) (layer "F.SilkS")
    (effects (font (size 1 1) (thickness 0.15)))
  )
  
  (fp_text value "LCD_54.58x20.80" (at 0 {glass_height/2 + 2}) (layer "F.Fab")
    (effects (font (size 1 1) (thickness 0.15)))
  )
  
  (fp_text user "${{REFERENCE}}" (at 0 0) (layer "F.Fab")
    (effects (font (size 1 1) (thickness 0.15)))
  )
  
  # Glass outline on F.Fab layer
  (fp_line (start {-glass_width/2} {-glass_height/2}) (end {glass_width/2} {-glass_height/2}) 
    (stroke (width 0.1) (type solid)) (layer "F.Fab"))
  (fp_line (start {glass_width/2} {-glass_height/2}) (end {glass_width/2} {glass_height/2}) 
    (stroke (width 0.1) (type solid)) (layer "F.Fab"))
  (fp_line (start {glass_width/2} {glass_height/2}) (end {-glass_width/2} {glass_height/2}) 
    (stroke (width 0.1) (type solid)) (layer "F.Fab"))
  (fp_line (start {-glass_width/2} {glass_height/2}) (end {-glass_width/2} {-glass_height/2}) 
    (stroke (width 0.1) (type solid)) (layer "F.Fab"))
  
  # Silkscreen outline (slightly larger)
  (fp_line (start {-glass_width/2 - 0.2} {-glass_height/2 - 0.2}) (end {glass_width/2 + 0.2} {-glass_height/2 - 0.2}) 
    (stroke (width 0.12) (type solid)) (layer "F.SilkS"))
  (fp_line (start {glass_width/2 + 0.2} {-glass_height/2 - 0.2}) (end {glass_width/2 + 0.2} {glass_height/2 + 0.2}) 
    (stroke (width 0.12) (type solid)) (layer "F.SilkS"))
  (fp_line (start {glass_width/2 + 0.2} {glass_height/2 + 0.2}) (end {-glass_width/2 - 0.2} {glass_height/2 + 0.2}) 
    (stroke (width 0.12) (type solid)) (layer "F.SilkS"))
  (fp_line (start {-glass_width/2 - 0.2} {glass_height/2 + 0.2}) (end {-glass_width/2 - 0.2} {-glass_height/2 - 0.2}) 
    (stroke (width 0.12) (type solid)) (layer "F.SilkS"))
  
  # Pin 1 marker
  (fp_circle (center {start_x - 1} {glass_height/2 - 1}) (end {start_x - 0.5} {glass_height/2 - 1})
    (stroke (width 0.12) (type solid)) (fill none) (layer "F.SilkS"))
  
  # Courtyard
  (fp_line (start {-glass_width/2 - 0.5} {-glass_height/2 - 0.5}) (end {glass_width/2 + 0.5} {-glass_height/2 - 0.5}) 
    (stroke (width 0.05) (type solid)) (layer "F.CrtYd"))
  (fp_line (start {glass_width/2 + 0.5} {-glass_height/2 - 0.5}) (end {glass_width/2 + 0.5} {glass_height/2 + 0.5}) 
    (stroke (width 0.05) (type solid)) (layer "F.CrtYd"))
  (fp_line (start {glass_width/2 + 0.5} {glass_height/2 + 0.5}) (end {-glass_width/2 - 0.5} {glass_height/2 + 0.5}) 
    (stroke (width 0.05) (type solid)) (layer "F.CrtYd"))
  (fp_line (start {-glass_width/2 - 0.5} {glass_height/2 + 0.5}) (end {-glass_width/2 - 0.5} {-glass_height/2 - 0.5}) 
    (stroke (width 0.05) (type solid)) (layer "F.CrtYd"))
  
  # Pads
'''
    
    # Add pads
    for i in range(num_pins):
        pin_num = i + 1
        pin_x = start_x + i * pin_pitch
        pin_y = glass_height / 2
        pin_name = pin_names[i]
        
        footprint += f'''  (pad "{pin_num}" smd rect (at {pin_x:.3f} {pin_y:.3f}) (size {pad_width} {pad_height})
    (layers "F.Cu" "F.Paste" "F.Mask"))
'''
    
    # Add 3D model reference
    footprint += f'''  
  (model "${{KIPRJMOD}}/LCD_54.58x20.80_8Pin.step"
    (offset (xyz 0 0 0))
    (scale (xyz 1 1 1))
    (rotate (xyz 0 0 0))
  )
)
'''
    
    return footprint


def generate_step_model():
    """Generate Python code using OCP (CadQuery) to create STEP model"""
    
    step_code = '''"""
STEP 3D Model Generator for LCD Display
Requires: cadquery (pip install cadquery)
Run this to generate: LCD_54.58x20.80_8Pin.step
"""

import cadquery as cq

# Dimensions
glass_width = 54.58
glass_height = 20.80
glass_thickness = 1.10

num_pins = 8
pin_pitch = 1.27
pin_width = 0.6
pin_depth = 1.5
pin_height = 12.0

# Calculate pin positions
total_pin_width = (num_pins - 1) * pin_pitch
start_x = -total_pin_width / 2

# Create glass body
glass = (cq.Workplane("XY")
    .box(glass_width, glass_height, glass_thickness)
    .edges("|Z")
    .fillet(0.5))

# Create pins
pins = cq.Workplane("XY").workplane(offset=-pin_height)

for i in range(num_pins):
    pin_x = start_x + i * pin_pitch
    pin_y = glass_height / 2
    
    pin = (cq.Workplane("XY")
        .workplane(offset=-pin_height)
        .center(pin_x, pin_y)
        .box(pin_width, pin_depth, pin_height))
    
    pins = pins.union(pin)

# Combine and move glass to top
assembly = pins.union(glass.translate((0, 0, glass_thickness/2)))

# Export STEP file
assembly.val().exportStep("LCD_54.58x20.80_8Pin.step")

print("STEP model generated: LCD_54.58x20.80_8Pin.step")
'''
    
    return step_code


def generate_simplified_step():
    """Generate a simplified STEP creation guide without dependencies"""
    
    guide = '''# Simplified STEP Model Creation Guide

Since CadQuery requires installation, here's how to create the STEP model:

## Option 1: Using FreeCAD (Free, GUI-based)
1. Open FreeCAD
2. Create a Part Design Body
3. Create the glass:
   - Sketch: Rectangle 54.58 x 20.80 mm
   - Pad: 1.10 mm
   - Fillet edges: 0.5 mm radius
4. Create 8 pins at bottom, centered:
   - Position calculations: X from -4.445 to 4.445 mm, step 1.27 mm
   - Y position: 10.4 mm (half of glass height)
   - Z position: -12 mm (below glass)
   - Pin size: 0.6 x 1.5 x 12 mm each
5. Export as STEP: File > Export > STEP

## Option 2: Using OpenSCAD (Free, Code-based)
Save this code as lcd_model.scad:

```openscad
// LCD Display STEP Model

glass_width = 54.58;
glass_height = 20.80;
glass_thick = 1.10;

pin_pitch = 1.27;
pin_width = 0.6;
pin_depth = 1.5;
pin_height = 12;

// Glass body
translate([0, 0, 0])
    minkowski() {
        cube([glass_width-1, glass_height-1, glass_thick], center=true);
        sphere(r=0.5, $fn=20);
    }

// 8 pins centered on bottom
for(i = [0:7]) {
    translate([i*pin_pitch - 3.5*pin_pitch, glass_height/2, -pin_height/2])
        cube([pin_width, pin_depth, pin_height], center=true);
}
```

Then export to STEP using OpenSCAD's export feature.

## Pin Positions Reference:
Pin 1 (VOUT):  X = -4.445 mm
Pin 2 (CAP1N): X = -3.175 mm
Pin 3 (CAP2N): X = -1.905 mm
Pin 4 (VDD):   X = -0.635 mm
Pin 5 (VSS):   X =  0.635 mm
Pin 6 (SDA):   X =  1.905 mm
Pin 7 (SCL):   X =  3.175 mm
Pin 8 (RST):   X =  4.445 mm

All pins: Y = 10.4 mm, Z = -12 to 0 mm
'''
    
    return guide


# Generate all files
print("="*60)
print("KiCad Footprint for LCD Display")
print("="*60)
print("\n1. FOOTPRINT FILE (Save as: LCD_54.58x20.80_8Pin_1.27mm.kicad_mod)")
print("-"*60)
footprint = generate_kicad_footprint()
print(footprint)

print("\n" + "="*60)
print("2. STEP MODEL GENERATOR (Save as: generate_lcd_step.py)")
print("-"*60)
step_gen = generate_step_model()
print(step_gen)

print("\n" + "="*60)
print("3. SIMPLIFIED STEP MODEL GUIDE")
print("-"*60)
guide = generate_simplified_step()
print(guide)

print("\n" + "="*60)
print("SUMMARY")
print("="*60)
print("""
Files to create:
1. LCD_54.58x20.80_8Pin_1.27mm.kicad_mod - KiCad footprint file
2. LCD_54.58x20.80_8Pin.step - 3D STEP model

Footprint features:
- Glass outline: 54.58 x 20.80 mm
- 8 SMD pads, 1.27mm pitch, centered on bottom edge
- Pin 1 marker for orientation
- Proper silkscreen and courtyard layers
- 3D model reference included

STEP Model features:
- Glass body: 54.58 x 20.80 x 1.10 mm
- 8 pins: 0.6 x 1.5 x 12 mm (height extends below PCB)
- Rounded glass edges

Installation in KiCad:
1. Copy .kicad_mod to your project's footprint library
2. Place .step file in your project directory
3. Use footprint in PCB editor
""")
