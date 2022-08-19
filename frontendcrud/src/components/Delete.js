import React from 'react'
import {Modal, Button, Input, Form} from 'antd'
import "antd/dist/antd.css";

const Delete = ({ deleteMethod, changeDeleteMethod, methodDelete, users}) => {
  return (
    <div>
        <Modal
        visible={deleteMethod}
        onCancel={changeDeleteMethod}
        centered
        footer={[
          <Button onClick={changeDeleteMethod}>No</Button>,
          <Button type="primary" danger onClick={methodDelete}>
            Yes
          </Button>,
        ]}
      >
        Do you want to delete <b>{users && users.name}</b> ?
      </Modal>
    </div>
  )
}

export default Delete