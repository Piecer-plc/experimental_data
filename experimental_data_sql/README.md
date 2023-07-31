We upload our all experimental data to google drive.The sql size are 20GB+.

Download: [click](https://drive.google.com/drive/folders/1oQNFGIdADov5HYrEFIhRJwuFw9h6rk93?usp=drive_link)

### Table

- api_label
- api_method
- compete
- compete_evaluate_algorithm
- dependencies_pool

- experimental_record
- experimental_record_valid
- ml_api
- ml_libraries
- output_evaluate
- output_evaluate_valid
- package
- pipeline
- run_pipeline_state
- run_pipeline_state_valid
- venv_install_info
- venv_install_info_valid

### SQl Example

- select the variant library version combinations.

  ```sql
  select * from venv_install_info where pipeline_id = '' where fixed_type=0
  ```

  

- select the pipeline run state.

  ```sql
  select * from experimental_record where pipeline_id = ''
  ```

  

- select the pipeline output evaluate.

  ```sql
  select * from output_evaluate where pipeline_id = ''
  ```

  