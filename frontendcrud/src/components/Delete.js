import React from 'react'
import {Modal, Button, Input, Form} from 'antd'
import "antd/dist/antd.css";

const Delete = ({ del, changeDel, delMethod, users}) => {
  return (
    <div>
        <Modal visible={del} onCancel={changeDel} centered footer={[
          <Button onClick={changeDel}>No</Button>,
          <Button type="primary" danger onClick={delMethod}>Yes</Button>
        ]}>
        Do you want to delete <b>{users && users.name}</b> ?</Modal>
    </div>
  )
}

export default Delete