<script>
    function toggle_avg(checkbox) (
        if (checkbox.checked) {
            searchvalue=".png";
            newvalue="_c14davg.png";
        } else {
            searchvalue="_c14davg.png";
            newvalue=".png";
        }
        images=document.getElementsByTagName("img")
        for(var i=0; i< images.length; i++) {
            images[i].src=images[i].src.replace(searchvalue,newvalue);
        }
    )
</script>

<input type="checkbox" onchange="toggle_avg(this);" checked> Use 14 day average
## Confirmed infections

### Top 10 Countries

![Graph of infections of top 10 countries](confirmed_c14davg.png)

### Top 10 US States

![Graph of infections of top 10 US states](confirmed_US_c14davg.png)

## Deaths

### Top 10 Countries

![Graph of deaths of top 10 countries](deaths_c14davg.png)

### Top 10 US States

![Graph of deaths of top 10 US states](deaths_US_c14davg.png)

## Active infections

### Top 10 Countries

![Graph of infected of top 10 countries](infected_c14davg.png)

### Top 10 US States

![Graph of infected of top 10 US states](infected_US_c14davg.png)
