# Lab 1: OneAgent Plugins

<br>
<br>

## Task 1: Preparing a host to monitor

### Step 1.1: Setup a Google Cloud Compute Engine instance:

Setup instance in Google:

- Name: instance-oneagentplugins
- Machine type: 2vCPU (7.5 GB memory, n1-standard-2)
- Image: Debian GNU/Linux 9 (stretch)
- Allow HTTP traffic
- Allow HTTPS traffic

<br>

### Step 1.2: Connect to instance:

Connect to instance:

Copy gcloud command from Google and paste it into your terminal.

<br>

### Step 1.3: Install git:

Execute this command on instance-oneagentplugins:

```
sudo apt-get install git
```

<br>

### Step 1.4: Clone repository:

Execute this command on instance-oneagentplugins:

```
git clone https://github.com/sachsenhofer/extending-monitoring.git
```

<br>
<br>

## Task 2: Deploy Dynatrace

### Step 2.1: Deploy Dynatrace:

Deploy Dynatrace on instance-oneagentplugins.

<br>
<br>

## Task 3: Build and deploy an OneAgent Plugin

### Step 3.1: Get superuser permissions:

Execute this command on instance-oneagentplugins:

```
sudo su
```

<br>

### Step 3.2: Install OneAgent SDK:

Execute this command on instance-oneagentplugins:

```
pip3 install oneagent_sdk-1.147.90.20180611.134001-py3-none-any.whl 
```

<br>

### Step 3.3: Develop plugin:

Develop plugin.

<br>

### Step 3.4: Create upload token:

In Dynatrace create a upload token:

#settings/monitoredtechnologies/addextension/addlocal

<br>

### Step 3.5: Build and upload plugin:

Execute this command on instance-oneagentplugins:

```
oneagent_build_plugin
```

Then enter the upload token when prompted.

If the command oneagent_build_plugin is not found you have to add the directory containing the executable to PATH:

```
$ sudo find / -name "oneagent_build_plugin"
/home/dominik.sachsenhofer/.local/bin/oneagent_build_plugin

$ export PATH=$PATH:/home/dominik.sachsenhofer/.local/bin
```

<br>

### Step 3.6: Upgrade plugin to production:

Upgrade plugin to production.

<br>

### Step 3.7: Run the demo application:

Execute this command on instance-oneagentplugins:

```
python3 -m oneagent_sdk.demo_app
```

<br>

### Step 3.8: Go to Dynatrace:

Go to Dynatrace and watch metrics coming in.

