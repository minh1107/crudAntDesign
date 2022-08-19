import React from "react";
import { Modal, Button, Input, Form } from "antd";
import "antd/dist/antd.css";
import './main.css'

const { Item } = Form;
const Edit = ({
  users,
  editMethod,
  changeEditMethod,
  putMethod,
  handleChange,
  handleChangeCompanyName
}) => {
  return (
    <div>
      <Modal
        width="60%"
        visible={editMethod}
        title="Edit user"
        onCancel={changeEditMethod}
        centered
        footer={[
          <Button onClick={changeEditMethod}>Cancel</Button>,
          <Button type="primary" onClick={putMethod}>
            Edit
          </Button>
        ]}
      >
        <Form
           labelCol={{
            span: 4,
          }}
          wrapperCol={{
            span: 18,
          }}
        >
          <Item label="Name">
            <Input
              disabled="false"
              name="name"
              onChange={handleChange}
              value={users && users.name}
            />
          </Item>
          <Item label="Username">
            <Input
              disabled="false"
              name="username"
              onChange={handleChange}
              value={users && users.username}
            />
          </Item>
          <Item label="Email">
            <Input
              name="email"
              onChange={handleChange}
              value={users && users.email}
            />
          </Item>
          <Item label="Phone">
            <Input
              name="phone"
              onChange={handleChange}
              value={users && users.phone}
            />
          </Item>
          <Item label="Website">
            <Input
              name="website"
              onChange={handleChange}
              value={users && users.website}
            />
          </Item>
          <Item className="bold_text" label="Address"/>
          <Form
             labelCol={{
              span: 4,
            }}
            wrapperCol={{
              span: 18,
            }}
          >
            <Item label="Street">
              <Input
                name="addressstreet"
                onChange={handleChange}
                value={users && users.addressstreet}
              />
            </Item>
            <Item label="Suite">
              <Input
                name="addresssuite"
                onChange={handleChange}
                value={users && users.addresssuite}
              />
            </Item>
            <Item label="City">
              <Input
                name="addresscity"
                onChange={handleChange}
                value={users && users.addresscity}
              />
            </Item >
            <Item label="Zip code">
              <Input
                name="addresszipcode"
                onChange={handleChange}
                value={users && users.addresszipcode}
              />
            </Item>
          </Form>
          <Item label="Company" className="bold_text"/>
          <Form 
             labelCol={{
              span: 4,
            }}
            wrapperCol={{
              span: 18,
            }}
          >
            <Item label="Name">
                <Input
                         name="companyname"
                         onChange={handleChangeCompanyName}
                         value={users && users.companyname}
                >
                </Input>
            </Item>
            <Item label="Catch Phrase">
                <Input
                         name="companycatchphrase"
                         onChange={handleChange}
                         value={users && users.companycatchphrase}
                >
                </Input>
            </Item>
            <Item label="business">
                <Input
                         name="companybs"
                         onChange={handleChange}
                         value={users && users.companybs}
                >
                </Input>
            </Item>
          </Form>
        </Form>
      </Modal>
    </div>
  );
};

export default Edit;
