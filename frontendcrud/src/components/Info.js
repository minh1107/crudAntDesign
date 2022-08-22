import { Table, Descriptions  } from 'antd'
import React from 'react'

const Info = ({users}) => {
  return (
    <div>
        <Descriptions title="">
        <Descriptions.Item label="UserName">{users.username || "No data"}</Descriptions.Item>
        <Descriptions.Item label="Email">{users.email || "No data"}</Descriptions.Item>
        <Descriptions.Item label="Telephone">{users.phone || "No data"}</Descriptions.Item>
        <Descriptions.Item label="Website">{users.website || "No data"}</Descriptions.Item>
        <Descriptions.Item label="Address">
        Street: {users.addressstreet || "No data"} <br/>
        Suite: {users.addresssuite || "No data"} <br/>
        City: {users.addresscity || "No data"} <br/>
        Zip code: {users.addresszipcode || "No data"}
        </Descriptions.Item>
        <Descriptions.Item label="Company">
        Name: {users.companyname || "No data"} <br/>
        Catch Phrase: {users.companycatchphrase || "No data"} <br/>
        Business: {users.companycatchphrase || "No data"} 
        </Descriptions.Item>
        </Descriptions>
    </div>
  )
}

export default Info