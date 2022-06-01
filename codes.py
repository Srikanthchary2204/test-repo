

import apache_beam as beam
import sys


argv=[
    '--project=demo1-348613'
    '--job_name=hdh'
    '--region=us-central'
    '--staging_location=gs://demotabl/'
    '--temp_location=gs://demotabl/'
    '--runner=DataFlowRunner'
    
]
if __name__ == '__main__':
    
   p = beam.Pipeline(argv=sys.argv)
   input = 'gs://demotabl/addresses.csv'
   output_prefix = 'demo1-348613:tobq.ty'
   def to_json(csv_str):
       fields = csv_str
       json_str={"name": fields,
              "SR": fields,
              "AD": fields,
              "GG": fields,
              "FGG": fields,
              "PIN": fields}
       return json_str
    

   sch="name:STRING,SR:STRING,AD:STRING,GG:STRING,FGG:STRING,PIN:STRING"

   # find all lines that contain the searchTerm
   (p
      | 'GetJava' >> beam.io.ReadFromText(input)
      |'to json'>> beam.Map(to_json)
      | 'write' >> beam.io.WriteToBigQuery(output_prefix,schema=sch,create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE,custom_gcs_temp_location="gs://demotabl/")
   )

   p.run().wait_until_finish()

