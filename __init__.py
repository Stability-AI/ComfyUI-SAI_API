from .stability_api import StabilityConservativeUpscale, StabilityCreativeUpscale, StabilityRemoveBackground, StabilityInpainting, StabilityErase, StabilityCore, StabilitySearchAndReplace, StabilityOutpainting, StabilitySD3, StabilityControlSketch, StabilityControlStructure

NODE_CLASS_MAPPINGS = {
    "Stability Conservative Upscale": StabilityConservativeUpscale,
    "Stability Creative Upscale": StabilityCreativeUpscale,
    "Stability Remove Background": StabilityRemoveBackground,
    "Stability Erase": StabilityErase,
    "Stability Inpainting": StabilityInpainting,
    "Stability Image Core": StabilityCore,
    "Stability Search and Replace": StabilitySearchAndReplace,
    "Stability Outpainting": StabilityOutpainting,
    "Stability SD3": StabilitySD3,
    "Stability Control Skech": StabilityControlSketch,
    "Stability Control Structure": StabilityControlStructure,
}
