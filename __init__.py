from .stability_api import StabilityConservativeUpscale, StabilityCreativeUpscale, StabilityRemoveBackground, StabilityInpainting, StabilityErase, StabilityCore, StabilityImageUltra, StabilitySearchAndReplace, StabilityOutpainting, StabilitySD3, StabilityControlSketch, StabilityControlStructure, StabilityFastUpscale, StabilityControlStyle, StabilitySearchAndRecolor

NODE_CLASS_MAPPINGS = {
    "Stability Conservative Upscale": StabilityConservativeUpscale,
    "Stability Creative Upscale": StabilityCreativeUpscale,
    "Stability Remove Background": StabilityRemoveBackground,
    "Stability Erase": StabilityErase,
    "Stability Inpainting": StabilityInpainting,
    "Stability Image Core": StabilityCore,
    "Stability Image Ultra": StabilityImageUltra,
    "Stability Search and Replace": StabilitySearchAndReplace,
    "Stability Outpainting": StabilityOutpainting,
    "Stability SD3": StabilitySD3,
    "Stability Control Sketch": StabilityControlSketch,
    "Stability Control Structure": StabilityControlStructure,
    "Stability Fast Upscale": StabilityFastUpscale,
    "Stability Style": StabilityControlStyle,
    "Stability Search and Recolor": StabilitySearchAndRecolor,
}