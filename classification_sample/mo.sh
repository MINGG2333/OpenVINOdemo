python3 /opt/intel/openvino/deployment_tools/model_optimizer/mo.py \
    --input_model=inception_layers.iv3.pb \
    --input_shape=[1,299,299,3] \
    --output_dir=.\
    --data_type=FP16
