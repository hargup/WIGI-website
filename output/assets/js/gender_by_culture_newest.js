(function(global) {
  if (typeof (window._bokeh_onload_callbacks) === "undefined"){
    window._bokeh_onload_callbacks = [];
  }
  function load_lib(url, callback){
    window._bokeh_onload_callbacks.push(callback);
    if (window._bokeh_is_loading){
      console.log("Bokeh: BokehJS is being loaded, scheduling callback at", new Date());
      return null;
    }
    console.log("Bokeh: BokehJS not loaded, scheduling load and callback at", new Date());
    window._bokeh_is_loading = true;
    var s = document.createElement('script');
    s.src = url;
    s.async = true;
    s.onreadystatechange = s.onload = function(){
      Bokeh.embed.inject_css("http://cdn.pydata.org/bokeh/release/bokeh-0.10.0.min.css");
      window._bokeh_onload_callbacks.forEach(function(callback){callback()});
    };
    s.onerror = function(){
      console.warn("failed to load library " + url);
    };
    document.getElementsByTagName("head")[0].appendChild(s);
  }

  bokehjs_url = "http://cdn.pydata.org/bokeh/release/bokeh-0.10.0.min.js"

  var elt = document.getElementById("d3cb47d0-9f07-4c71-8e0b-f1f96dd84efa");
  if(elt==null) {
    console.log("Bokeh: ERROR: autoload.js configured with elementid 'd3cb47d0-9f07-4c71-8e0b-f1f96dd84efa' but no matching script tag was found. ")
    return false;
  }

  // These will be set for the static case
  var all_models = [{"attributes": {"plot": {"subtype": "LegacyChart", "type": "Plot", "id": "1277c690-d86f-47f5-831c-3044e3e462ac"}, "tags": [], "doc": null, "id": "1517cf78-e6b3-422e-a7ab-d1b3a82a4ef9"}, "type": "ResetTool", "id": "1517cf78-e6b3-422e-a7ab-d1b3a82a4ef9"}, {"attributes": {"column_names": ["width_cat", "catmale", "stackedfemale", "midfemale", "catfemale", "cat", "stackedmale", "width", "zero", "female", "male", "midmale"], "tags": [], "doc": null, "selected": {"2d": {"indices": []}, "1d": {"indices": []}, "0d": {"indices": [], "flag": false}}, "callback": null, "data": {"width_cat": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2], "catmale": ["africa:0.666666666667", "south asia:0.666666666667", "islamic:0.666666666667", "latin america:0.666666666667", "orthodox:0.666666666667", "confucian:0.666666666667", "catholic european:0.666666666667", "protestant european:0.666666666667", "english-speaking:0.666666666667"], "stackedfemale": [1669.5, 3428.0, 3599.0, 7650.0, 9516.5, 13202.5, 24932.5, 34998.5, 41873.5], "midfemale": [1669.5, 3428.0, 3599.0, 7650.0, 9516.5, 13202.5, 24932.5, 34998.5, 41873.5], "catfemale": ["africa:0.333333333333", "south asia:0.333333333333", "islamic:0.333333333333", "latin america:0.333333333333", "orthodox:0.333333333333", "confucian:0.333333333333", "catholic european:0.333333333333", "protestant european:0.333333333333", "english-speaking:0.333333333333"], "cat": ["africa", "south asia", "islamic", "latin america", "orthodox", "confucian", "catholic european", "protestant european", "english-speaking"], "stackedmale": [13546.5, 21162.0, 27798.5, 56619.5, 74188.5, 53943.0, 211641.5, 240738.0, 288659.5], "width": [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8], "zero": [23754.0, 35468.0, 48399.0, 97939.0, 129344.0, 81481.0, 373418.0, 411479.0, 493572.0], "female": [3339, 6856, 7198, 15300, 19033, 26405, 49865, 69997, 83747], "male": [20415, 28612, 41201, 82639, 110311, 55076, 323553, 341482, 409825], "midmale": [10207.5, 14306.0, 20600.5, 41319.5, 55155.5, 27538.0, 161776.5, 170741.0, 204912.5]}, "id": "4bc278f9-2a8e-4ae5-be55-423e158f130f"}, "type": "ColumnDataSource", "id": "4bc278f9-2a8e-4ae5-be55-423e158f130f"}, {"attributes": {"geometries": [], "tags": [], "doc": null, "id": "36efd8a7-a60c-414e-93a3-4499cbe722c8"}, "type": "ToolEvents", "id": "36efd8a7-a60c-414e-93a3-4499cbe722c8"}, {"attributes": {"end": 542929.20000000007, "callback": null, "doc": null, "tags": [], "start": 0, "id": "20ba8610-5790-4039-9048-819c74c9b232"}, "type": "Range1d", "id": "20ba8610-5790-4039-9048-819c74c9b232"}, {"attributes": {"plot": {"subtype": "LegacyChart", "type": "Plot", "id": "1277c690-d86f-47f5-831c-3044e3e462ac"}, "tags": [], "doc": null, "id": "b212f4d2-7b60-4001-b232-ab5f3074c151"}, "type": "HelpTool", "id": "b212f4d2-7b60-4001-b232-ab5f3074c151"}, {"attributes": {"nonselection_glyph": null, "data_source": {"type": "ColumnDataSource", "id": "4bc278f9-2a8e-4ae5-be55-423e158f130f"}, "tags": [], "doc": null, "selection_glyph": null, "id": "af13bf2d-1b85-4a86-a8c9-213da892d26f", "glyph": {"type": "Rect", "id": "a383b7c1-c547-45e8-a9e6-309359f1f6a8"}}, "type": "GlyphRenderer", "id": "af13bf2d-1b85-4a86-a8c9-213da892d26f"}, {"attributes": {"plot": {"subtype": "LegacyChart", "type": "Plot", "id": "1277c690-d86f-47f5-831c-3044e3e462ac"}, "tags": [], "doc": null, "id": "77da12b8-80c2-411c-8559-5308cfb8310a"}, "type": "ResizeTool", "id": "77da12b8-80c2-411c-8559-5308cfb8310a"}, {"attributes": {"plot": {"subtype": "LegacyChart", "type": "Plot", "id": "1277c690-d86f-47f5-831c-3044e3e462ac"}, "tags": [], "doc": null, "dimension": 1, "ticker": {"type": "BasicTicker", "id": "ef14b555-48e5-49eb-bd10-150737c1545e"}, "id": "ce60b83e-d8aa-4b84-93fe-bc3dfa3a23b8"}, "type": "Grid", "id": "ce60b83e-d8aa-4b84-93fe-bc3dfa3a23b8"}, {"attributes": {"nonselection_glyph": null, "data_source": {"type": "ColumnDataSource", "id": "4bc278f9-2a8e-4ae5-be55-423e158f130f"}, "tags": [], "doc": null, "selection_glyph": null, "id": "14f2096a-8b8a-42a6-b4c9-e9db4aebf478", "glyph": {"type": "Rect", "id": "a36b4404-ec6b-4a23-8f0f-d556beb9c289"}}, "type": "GlyphRenderer", "id": "14f2096a-8b8a-42a6-b4c9-e9db4aebf478"}, {"attributes": {"plot": {"subtype": "LegacyChart", "type": "Plot", "id": "1277c690-d86f-47f5-831c-3044e3e462ac"}, "dimensions": ["width", "height"], "tags": [], "doc": null, "id": "09dbf510-31f9-45f1-beef-d50fe8fa1ecb"}, "type": "BoxZoomTool", "id": "09dbf510-31f9-45f1-beef-d50fe8fa1ecb"}, {"attributes": {"doc": null, "id": "ed9dcaa8-d695-45e2-9b5a-5b8e0955ef55", "tags": []}, "type": "CategoricalTickFormatter", "id": "ed9dcaa8-d695-45e2-9b5a-5b8e0955ef55"}, {"attributes": {"line_color": {"value": "white"}, "fill_color": {"value": "#f22c40"}, "tags": [], "doc": null, "fill_alpha": {"value": 0.7}, "height": {"units": "data", "field": "female"}, "width": {"units": "data", "field": "width"}, "y": {"field": "stackedfemale"}, "x": {"field": "cat"}, "id": "a36b4404-ec6b-4a23-8f0f-d556beb9c289"}, "type": "Rect", "id": "a36b4404-ec6b-4a23-8f0f-d556beb9c289"}, {"attributes": {"tags": [], "doc": null, "mantissas": [2, 5, 10], "id": "ef14b555-48e5-49eb-bd10-150737c1545e"}, "type": "BasicTicker", "id": "ef14b555-48e5-49eb-bd10-150737c1545e"}, {"attributes": {"plot": {"subtype": "LegacyChart", "type": "Plot", "id": "1277c690-d86f-47f5-831c-3044e3e462ac"}, "orientation": "top_left", "tags": [], "doc": null, "id": "b56e92e8-47f1-4395-a05a-aeb2e46c478d", "legends": [["female", [{"type": "GlyphRenderer", "id": "14f2096a-8b8a-42a6-b4c9-e9db4aebf478"}]], ["male", [{"type": "GlyphRenderer", "id": "af13bf2d-1b85-4a86-a8c9-213da892d26f"}]]]}, "type": "Legend", "id": "b56e92e8-47f1-4395-a05a-aeb2e46c478d"}, {"attributes": {"doc": null, "id": "fc81e506-26d7-4a57-aa75-6bbe4d86e8db", "tags": []}, "type": "CategoricalTicker", "id": "fc81e506-26d7-4a57-aa75-6bbe4d86e8db"}, {"attributes": {"plot": {"subtype": "LegacyChart", "type": "Plot", "id": "1277c690-d86f-47f5-831c-3044e3e462ac"}, "tags": [], "doc": null, "id": "50bb1fcb-2f95-4164-84be-edc3ef97b8b8"}, "type": "PreviewSaveTool", "id": "50bb1fcb-2f95-4164-84be-edc3ef97b8b8"}, {"attributes": {"plot": {"subtype": "LegacyChart", "type": "Plot", "id": "1277c690-d86f-47f5-831c-3044e3e462ac"}, "tags": [], "doc": null, "major_label_orientation": 0.7853981633974483, "axis_label": "Culture", "formatter": {"type": "CategoricalTickFormatter", "id": "ed9dcaa8-d695-45e2-9b5a-5b8e0955ef55"}, "ticker": {"type": "CategoricalTicker", "id": "fc81e506-26d7-4a57-aa75-6bbe4d86e8db"}, "id": "9bb4cf81-101c-4de9-9d65-8c7905baa16a"}, "type": "CategoricalAxis", "id": "9bb4cf81-101c-4de9-9d65-8c7905baa16a"}, {"subtype": "LegacyChart", "type": "Plot", "id": "1277c690-d86f-47f5-831c-3044e3e462ac", "attributes": {"x_range": {"type": "FactorRange", "id": "2fb171dd-515b-4f2f-a203-db69c4dcd266"}, "right": [], "above": [], "tags": [], "tools": [{"type": "PanTool", "id": "a2747fad-1d2b-4e71-af66-509f7fc9b384"}, {"type": "WheelZoomTool", "id": "e450faf2-ae41-4bbd-8141-3bd71189ba71"}, {"type": "BoxZoomTool", "id": "09dbf510-31f9-45f1-beef-d50fe8fa1ecb"}, {"type": "PreviewSaveTool", "id": "50bb1fcb-2f95-4164-84be-edc3ef97b8b8"}, {"type": "ResizeTool", "id": "77da12b8-80c2-411c-8559-5308cfb8310a"}, {"type": "ResetTool", "id": "1517cf78-e6b3-422e-a7ab-d1b3a82a4ef9"}, {"type": "HelpTool", "id": "b212f4d2-7b60-4001-b232-ab5f3074c151"}], "id": "1277c690-d86f-47f5-831c-3044e3e462ac", "title": null, "renderers": [{"type": "CategoricalAxis", "id": "9bb4cf81-101c-4de9-9d65-8c7905baa16a"}, {"type": "LinearAxis", "id": "c6c9ff61-b6c2-4bdc-9823-f7393fed5b95"}, {"type": "Grid", "id": "ce60b83e-d8aa-4b84-93fe-bc3dfa3a23b8"}, {"type": "GlyphRenderer", "id": "14f2096a-8b8a-42a6-b4c9-e9db4aebf478"}, {"type": "GlyphRenderer", "id": "af13bf2d-1b85-4a86-a8c9-213da892d26f"}, {"type": "Legend", "id": "b56e92e8-47f1-4395-a05a-aeb2e46c478d"}], "plot_width": 800, "extra_y_ranges": {}, "extra_x_ranges": {}, "tool_events": {"type": "ToolEvents", "id": "36efd8a7-a60c-414e-93a3-4499cbe722c8"}, "plot_height": 500, "doc": null, "responsive": false, "y_range": {"type": "Range1d", "id": "20ba8610-5790-4039-9048-819c74c9b232"}, "below": [{"type": "CategoricalAxis", "id": "9bb4cf81-101c-4de9-9d65-8c7905baa16a"}], "left": [{"type": "LinearAxis", "id": "c6c9ff61-b6c2-4bdc-9823-f7393fed5b95"}]}}, {"attributes": {"plot": {"subtype": "LegacyChart", "type": "Plot", "id": "1277c690-d86f-47f5-831c-3044e3e462ac"}, "dimensions": ["width", "height"], "tags": [], "doc": null, "id": "a2747fad-1d2b-4e71-af66-509f7fc9b384"}, "type": "PanTool", "id": "a2747fad-1d2b-4e71-af66-509f7fc9b384"}, {"attributes": {"line_color": {"value": "white"}, "fill_color": {"value": "#5ab738"}, "tags": [], "doc": null, "fill_alpha": {"value": 0.7}, "height": {"units": "data", "field": "male"}, "width": {"units": "data", "field": "width"}, "y": {"field": "stackedmale"}, "x": {"field": "cat"}, "id": "a383b7c1-c547-45e8-a9e6-309359f1f6a8"}, "type": "Rect", "id": "a383b7c1-c547-45e8-a9e6-309359f1f6a8"}, {"attributes": {"plot": {"subtype": "LegacyChart", "type": "Plot", "id": "1277c690-d86f-47f5-831c-3044e3e462ac"}, "dimensions": ["width", "height"], "tags": [], "doc": null, "id": "e450faf2-ae41-4bbd-8141-3bd71189ba71"}, "type": "WheelZoomTool", "id": "e450faf2-ae41-4bbd-8141-3bd71189ba71"}, {"attributes": {"format": "%5.1e", "doc": null, "tags": [], "id": "078b71f2-423b-4e93-be90-4b37f4c055f9"}, "type": "PrintfTickFormatter", "id": "078b71f2-423b-4e93-be90-4b37f4c055f9"}, {"attributes": {"callback": null, "factors": ["africa", "south asia", "islamic", "latin america", "orthodox", "confucian", "catholic european", "protestant european", "english-speaking"], "doc": null, "tags": [], "id": "2fb171dd-515b-4f2f-a203-db69c4dcd266"}, "type": "FactorRange", "id": "2fb171dd-515b-4f2f-a203-db69c4dcd266"}, {"attributes": {"plot": {"subtype": "LegacyChart", "type": "Plot", "id": "1277c690-d86f-47f5-831c-3044e3e462ac"}, "tags": [], "doc": null, "axis_label": "Total gendered biographies", "formatter": {"type": "PrintfTickFormatter", "id": "078b71f2-423b-4e93-be90-4b37f4c055f9"}, "ticker": {"type": "BasicTicker", "id": "ef14b555-48e5-49eb-bd10-150737c1545e"}, "id": "c6c9ff61-b6c2-4bdc-9823-f7393fed5b95"}, "type": "LinearAxis", "id": "c6c9ff61-b6c2-4bdc-9823-f7393fed5b95"}];

  if(typeof(Bokeh) !== "undefined") {
    console.log("Bokeh: BokehJS loaded, going straight to plotting");
    Bokeh.embed.inject_plot("d3cb47d0-9f07-4c71-8e0b-f1f96dd84efa", all_models);
  } else {
    load_lib(bokehjs_url, function() {
      console.log("Bokeh: BokehJS plotting callback run at", new Date())
      Bokeh.embed.inject_plot("d3cb47d0-9f07-4c71-8e0b-f1f96dd84efa", all_models);
    });
  }

}(this));