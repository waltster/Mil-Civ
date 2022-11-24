import tensorflow as tf

def main():
	saved_model_dir = "../model/inference_graph/saved_model"

	# Convert the model
	converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir) # path to the SavedModel directory
	converter.target_spec.supported_ops = [
		tf.lite.OpsSet.TFLITE_BUILTINS
	]
	tflite_model = converter.convert()

	# Save the model.
	with open('../model/inference_graph/model.tflite', 'wb') as f:
  		f.write(tflite_model)

if __name__ == "__main__":
	main()
