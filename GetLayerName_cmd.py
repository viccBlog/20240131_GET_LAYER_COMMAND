from System.Windows.Forms import Clipboard

import rhinoscriptsyntax as rs

__commandname__ = "GetLayer"


def format_layers(layers):
  
  tmp_text = ""
  
  for i in xrange(len(layers)):
    
    layer = layers[i]
    
    if i == 0:
      tmp_text = tmp_text + layer
    else:
      tmp_text = tmp_text + "\n" + layer
      
  return tmp_text


def objs_to_layer(objs):
  
  layers = []
  
  ### Get Layers
  for obj in objs:
    layers.append(rs.ObjectLayer(obj))
  
  ### Remove Duplicate
  layers_set = list(set(layers))
  
  return layers_set


def to_clipboad(layers):
    
    text_copy = format_layers(layers)
    Clipboard.SetText(text_copy)
    
    
    print(text_copy)


# RunCommand is the called when the user enters the command name in Rhino.
# The command name is defined by the filname minus "_cmd.py"
def RunCommand( is_interactive ):
  
  VERSION = "2.0.0.0"
  print("***RUN GetLayer (ver {})".format(VERSION))
  
  objs = rs.SelectedObjects()
  
  
  ### Case A
  if len(objs) >= 1:
    
    layers_set = objs_to_layer(objs)
    to_clipboad(layers_set)

  ### Case B
  else:
    
    objs_new = rs.GetObjects(message="***Please Select Objects :")
    ### print(objs_new)
    
    ### to Ignore Case
    ###     - When processing is interrupted (Press ESC key)
    ###     - Not Selected
    
    if objs_new != None:
      layers_set = objs_to_layer(objs_new)
      to_clipboad(layers_set)
  
  # you can optionally return a value from this function
  # to signify command result. Return values that make
  # sense are
  #   0 == success
  #   1 == cancel
  # If this function does not return a value, success is assumed
  return 0
