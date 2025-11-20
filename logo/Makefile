
logo:
	# MetalTop_Label: 53/10
	python3 make_gds.py --cellname logo --scale 0.2 --pixel-size 5.0 --threshold 128 --layer 53 --datatype 10 --invert --merge raw/logo.png gds/logo.gds

	# MetalTop_Slot: 53/3
	python3 make_gds.py --cellname logo_nofill --scale 0.2 --pixel-size 2.0 --threshold 128 --layer 53 --datatype 3 --invert --merge raw/logo_nofill.png gds/logo_nofill.gds

	python3 combine_gds.py gds/logo.gds gds/logo_nofill.gds gds/logo_combined.gds

.PHONY: logo
